from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}

def get_date(prompt, allow_default=False):  # Getting time from user and formatting it
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)  # If user doesn't enter a date, returns today's date

    try:
        valid_date = datetime.strptime(date_str, date_format)  # formatting
        return valid_date.strftime(date_format) # Returns formatted user input
    except ValueError:
        print("Invalid date format. Please enter your date in dd-mm-yyyy format.")
        return get_date(prompt, allow_default)  # Makes the function recursive

def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("The amount cannot be zero or a negative value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()


def get_category():
    category = input("Enter the category ('I' for income, 'E' for expense.)").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]

    print("Invalid category. Please enter 'I' for income, or 'E' for expense.")
    return get_category()

def get_description():
    return input("Enter a description. (optional): ")