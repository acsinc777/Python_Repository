from datetime import datetime

print("ALEDUK5688 Spreadsheet Automation Menu")

print("Choose one of the numbered options.")
print()
print("1.) Input Data")
print("2.) View Current Data")
print("3.) Generate Report")

#The next line retrieves the inputted option and stores into the variable called 'Choice'
choice = int(input("Make your selection: "))

print(f'Option {choice} was selected at', str(datetime.now()))
