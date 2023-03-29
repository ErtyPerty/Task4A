import datetime
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime as dt

df = pd.read_csv('Task_4a_data.csv', index_col='ID')

# main menu with input sanitization
def menu():
    while True:
        try:
            print("\t\t****MAIN MENU****")
            print('1) Enter sales records')
            print('2) Run reports')
            x = int(input("Enter your choice (1 or 2): "))
            if x not in [1, 2]:
                raise ValueError
            return x
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")

# reports menu with input sanitization
def menu2():
    while True:
        try:
            print("**** Reports Dashboard ****")
            print("1. Individual Employee Report")
            x = int(input("Enter your choice (1): "))
            if x != 1:
                raise ValueError
            return x
        except ValueError:
            print("Invalid input. Please enter 1.")

def check_employment(df, id, start_date, end_date):
    # Make a copy of the original dataframe to avoid modifying it
    df_copy = df.copy()

    # Filter by ID
    df_copy = df_copy.loc[df_copy['ID'] == id]

    # Transpose and remove unnecessary rows
    df_copy = df_copy.T[3:]

    # Reset index and convert dates to datetime objects
    df_copy.reset_index(inplace=True)
    df_copy.rename(columns={'index': 'Date'}, inplace=True)
    df_copy['Date'] = pd.to_datetime(df_copy['Date'], format='%d/%m/%Y')
    start_date = pd.to_datetime(start_date, format='%d/%m/%Y')
    end_date = pd.to_datetime(end_date, format='%d/%m/%Y')

    # Filter by date range
    mask = (df_copy['Date'] >= start_date) & (df_copy['Date'] <= end_date)
    df_search = df_copy.loc[mask]

    # Print total and plot results
    total = df_search[id].sum()
    print('Total for ID {} is {}'.format(id, total))

    plt.bar(df_search['Date'], df_search[id])
    plt.xticks(rotation=90)
    plt.show()


y = menu()
while y == 1 or y == 2:
    if y == 1:
        try:
            ID = int(input("Enter the Staff ID "))
            if ID not in df.index.values:
                print('yes')

            date1 = input("Enter Date in dd/mm/yy: ")
            day, month, year = date1.split("/")
            date1 = datetime.date(int(year), int(month), int(day))

            if datetime.datetime.strptime(date1.strftime('%d/%m/%Y'), '%d/%m/%Y') > datetime.datetime.strptime(
                    dt.today().strftime('%d/%m/%Y'), '%d/%m/%Y'):
                print("Date is in the future")
            else:
                cost = float(input("Enter the cost : "))
                df.loc[ID, date1.strftime('%d/%m/%Y')] = cost
            # df.to_csv('test2.csv')
        except:
            print("\n\nError Occurred Please try again\n\n")
            y = menu()

    if y == 2:
        x = menu2()
        if x == 1:
            try:
                id = int(input("Enter the Employee Id : "))
                s_date = input("Enter Starting Date in dd/mm/yyyy: ")
                day, month, year = s_date.split("/")
                s_date = datetime.date(int(year), int(month), int(day))

                e_date = input("Enter Date in dd/mm/yyyy: ")
                day, month, year = e_date.split("/")
                e_date = datetime.date(int(year), int(month), int(day))

                s_date = datetime.datetime.strptime(s_date.strftime('%d/%m/%Y'), '%d/%m/%Y')
                e_date = datetime.datetime.strptime(e_date.strftime('%d/%m/%Y'), '%d/%m/%Y')
                ind_emp_check(df, id, s_date, e_date)
            except:
                print("\n\nError Occurred Please try again\n\n")
                x = menu2()

        else:
            x = menu2()
    else:
        x = menu()
    x = menu()
