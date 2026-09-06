# Student Info Request
studentName = input('Enter student name: ')
studentID = input('Enter student ID: ')

# Variables
num1 = int(input('Enter a whole number: '))
num2 = int(input('Enter another whole number: '))

addNums = num1 + num2
multiplyNums = num1 * num2
divideNums = num1 / num2

# Statements Containing Information
print(f'{studentName} | {studentID}')

if num1 > num2:
    print(f'{num1} is greater than {num2}')
elif num1 < num2:
    print(f'{num1} is less than {num2}')
elif num1 == num2:
    print(f'{num1} is equal to {num2}')

print(f'{num1} added with {num2} equals {addNums:,.2f}')
print(f'{num1} multiplied by {num2} equals {multiplyNums:,.2f}')
print(f'{num1} divided by {num2} equals {divideNums:,.2f}')
