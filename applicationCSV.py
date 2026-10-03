from datetime import datetime
import csv
import matplotlib.pyplot as plt

# This function inserts data into the .csv file
def insertData(path, data):
    try:
        with open(path, 'a') as f:
            f.write(data + "\n")
    except Exception as e:
        print("Error writing to file", e)

# This function reads and displays the contents stored in the .csv file
def viewData(path):
    try:
        with open(path, 'r') as f:
            print("File:", path)
            print(f.read())
    except Exception as e:
        print("Error reading file:", e)

# This function converts inches of rainfall into centimeters
def convertData(inches):
    centi = inches * 2.54
    return centi

# This function takes manual input to collect data
def getInput():
    counter = int(input("How many entries are you entering?: "))
    for i in range(counter):
        date = (input("Enter a date in the xx/xx/xxxx format: "))
        inches = float(input("Enter the rain amount in inches for the date: "))
        
        # Name of function being called is convertData() with inches being passed into it
        # Expected return value should be centi
        centi = convertData(inches)
        
        print(f'The following was saved at ', str(datetime.now()))
        print(f'{date} | {inches} | {centi}')

        data = f"{date},{inches},{centi}"

        insertData("ZooData.csv", data)

# This function is the main function
def main():
    print("ALEDUK5688 Spreadsheet Automation Menu")

    menuOptions = ["1.) Input Data", "2.) View Current Data", "3.)Generate Report"]
    count = 0

    #For loop will cycle through the menuOptions list, using count to list them out
    print("Choose one of the numbered options.")
    for count in menuOptions:
        print(count)

    #The next line retrieves the inputted option and stores into the variable called 'Choice'
    choice = int(input("Make your selection: "))
    valid = "Choice selected."

    if choice == 1:
        print(f'Option {choice} was selected at', str(datetime.now()))
    elif choice == 2:
        print(f'Option {choice} was selected at', str(datetime.now()))
    elif choice == 3:
        print(f'Option {choice} was selected at', str(datetime.now()))
    else:
        print("Incorrect Option Chosen.")

    if choice == 1:
        getInput()
    elif choice == 2:
        viewData("ZooData.csv")
    else:
        print("Error: The cosen functionality is not implemented yet.")

main()
