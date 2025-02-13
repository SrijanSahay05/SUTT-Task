import pandas as pd
import json

mess_menu_df = pd.read_excel("Mess Menu Sample.xlsx", sheet_name="Sheet1") # Importing the excel file as a pandas datafram
mess_menu_json = {}

def format_cell_value(cell_value):
    '''
    Function to format the cell value, like removing cell values witjh 
    only "*" and removing extra spaces between dish names
    '''
    if isinstance(cell_value, str):
        if set(cell_value.strip()) == {"*"}:
            return ""
        cell_value = " ".join(cell_value.split())
    return cell_value

def daily_menu(df):
    '''
    Function to extract the daily menu from the dataframe,
    and store it in a dictionary with the date as the key

    a loop runs over each column of the dataframe, and extracts the date (using the first row of the column)
    and the menu items for breakfast, lunch and dinner. 
    since the excel was in a format with exact number of rows from where different meal menu started, 
    I used the row numbers to extract the menu items for each meal.
    
    also there is a condition checking if the excel cell is empty, it it is then nothing is appened to the list, 
    before appending the menu format_cell_value is being called to remove extra spacing or unwanted entries such as "*".
    '''
    for col in range(df.shape[1]):
        daily_menu = {}
        breakfast_items = []
        lunch_items = []
        dinner_items = []
        date_str = df.iloc[0, col]
        formatted_date = date_str.strftime("%d-%m-%Y")

        for item in range(2, 11):
            cell_value = df.iloc[item, col]
            cell_value = format_cell_value(cell_value)
            if pd.isna(cell_value) or cell_value == "":
                cell_value = ""
            else:
                breakfast_items.append(cell_value)
        daily_menu["Breakfast"] = breakfast_items

        for item in range(13, 21):
            cell_value = df.iloc[item, col]
            cell_value = format_cell_value(cell_value)
            if pd.isna(cell_value) or cell_value == "":
                cell_value = ""
            else:
                cell_value = format_cell_value(cell_value)
                lunch_items.append(cell_value)
        daily_menu["Lunch"] = lunch_items

        for item in range(23, 30):
            cell_value = df.iloc[item, col]
            cell_value = format_cell_value(cell_value)
            if pd.isna(cell_value) or cell_value == "":
                cell_value = ""
            else:
                cell_value= format_cell_value(cell_value)
                dinner_items.append(cell_value)
        daily_menu["Dinner"] = dinner_items

        print(f"Menu for {formatted_date}: {daily_menu}")
        mess_menu_json[formatted_date] = daily_menu

    return mess_menu_json


def export_json(json_file):
    '''
    function to export the dictionary to a json file
    '''
    with open("mess_menu.json", "w") as json_file:
        json.dump(mess_menu_json, json_file, indent=4)


print(daily_menu(mess_menu_df))
export_json(mess_menu_json)
