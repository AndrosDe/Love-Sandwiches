import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPE_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

#This is the code to check if the API are correct linked:
#sales = SHEET.worksheet('sales')
#data = sales.get_all_values()
#print(data)

def get_sales_data():
    """
    Get sales figures input from the user

    """
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, seüerated by commas.")
    print("Example: 10,20,30,40,50,60")

    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")

get_sales_data()
