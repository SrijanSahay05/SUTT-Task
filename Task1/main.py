import pandas as pd
import json

mess_menu_df = pd.read_excel("Mess Menu Sample.xlsx", sheet_name="Sheet1")
mess_menu_json = {}


def daily_menu(df):
    for col in range(df.shape[1]):
        daily_menu = {}
        breakfast_items = []
        lunch_items = []
        dinner_items = []
        date_str = df.iloc[0, col]
        formatted_date = date_str.strftime("%d-%m-%Y")

        for item in range(2, 11):
            cell_value = df.iloc[item, col]
            if pd.isna(cell_value) or cell_value == "":
                break
            else:
                breakfast_items.append(cell_value)
        daily_menu["Breakfast"] = breakfast_items

        for item in range(13, 21):
            cell_value = df.iloc[item, col]
            if pd.isna(cell_value) or cell_value == "":
                break
            else:
                lunch_items.append(cell_value)
        daily_menu["Lunch"] = lunch_items

        for item in range(23, 30):
            cell_value = df.iloc[item, col]
            if pd.isna(cell_value) or cell_value == "":
                break
            else:
                dinner_items.append(cell_value)
        daily_menu["Dinner"] = dinner_items

        print(f"Menu for {formatted_date}: {daily_menu}")
        mess_menu_json[formatted_date] = daily_menu

    return mess_menu_json


def export_json(json_file):
    with open("mess_menu.json", "w") as json_file:
        json.dump(mess_menu_json, json_file, indent=4)


print(daily_menu(mess_menu_df))
export_json(mess_menu_json)

