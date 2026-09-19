from datetime import datetime

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
