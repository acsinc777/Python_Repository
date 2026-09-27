#ALEDUK5688
#9/24/2026
#2.7 Performance Assessment - Decisions, Loops, Processing, Output Formatting

name = input("Please enter your name: ")
studID = input("Please enter your Student ID: ")

number = 42
guess = 0
tries = 0

while guess != number:
    guess = int(input("Please guess a number between 1 and 100: "))
    tries += 1
    if guess > number:
        print("The number you entered was too high.")
    elif guess < number:
        print("The number you entered was too low.")
    elif guess == number:
        print(f"You guessed correctly, {name}. It took you {tries} attempt(s).")
    else:
        print("Please enter a valid number.")

counter = 0
incr = 0
print()
print("Output from While Loop:")
while counter < 5:
    counter += 1
    incr = counter + number
    print(f'{number} incrimented by {counter} is {incr}.')

counter = 0
incr = 0
print()
print("Output from For Loop:")
for i in range(5):
    counter += 1
    incr = counter + number
    print(f'{number} incrimented by {counter} is {incr}.')


