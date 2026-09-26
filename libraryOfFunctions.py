def functionOne():
    print("My Student ID is ALEDUK5688.")#outputs my Student ID

def functionTwo():
    n1 = int(input("Please enter a number. "))#enters first number to store
    n2 = int(input("Please enter another number. "))#enters second number to store
    sumNum = n1 + n2 #defines the sum
    print(f'The sum of {n1} and {n2} is {sumNum}.') #outputs the sum with both num variables
    return sumNum #function returns sum for use
             

def functionThree(sumNum): #accepts sumNum parameters
    if sumNum > 5:
        print("The sum is greater than 5.") #greater than comparison
    elif sumNum <= 5:
        print("The sum is 5 or less.") #equal or less then comparison
    numID = 5688 #defines numerical value of my Student ID
    return numID #returns numID for main() use


def main():
    functionOne() #functionOne called
    sumNum = functionTwo() #sumNum returned value to be sent to functionTwo
    numID = functionThree(sumNum) #numID returned value to be send to functionThree
    print(f'functionThree returned the value of {numID}.')

main()
