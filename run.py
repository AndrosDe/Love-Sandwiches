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
    while True:
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, seüerated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here: ")
        
        #to return the broken up values as list:
        sales_data = data_str.split(",")
        
        if validate_data(sales_data):
            print("Data is valid!")
            break


def validate_data(values):
    """
    Inside the try, converts all string values to intergrers.
    Raises ValueError if strings cannot be converted into int,
    or if there arent exactly 6 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    
    return True


get_sales_data()
