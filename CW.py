import random
def main():
    # problem1()
    # problem2()
    problem3()
    # problem4()
# Create a random number. Print the number.
def problem1():
    randomNum = random.randint(0, 10)
    print(randomNum)
# Create a function that has a loop that quits with ‘q’.
# If the user doesn't enter 'q', ask them to input another string.
def problem2():
    userInput = ""
    while userInput != "q":
        userInput = input("Enter a string\nEnter q to quit\n")
# Create a function that will loop until the user enters '0'.
# Ask the user to enter a positive integer number.
# Print 0 to that number and ask them again to enter a number until they enter '0'.
# Repeat.
def problem3():
    userInput = ""
    while userInput != 0:
        userInput =int(input("Enter a positive number\n"))
        if userInput != 0:
            for numbers in range(0, userInput+1):
                print(numbers)
# Create a function that creates a random number. Ask the user to guess the random number.
# Keep letting the user guess until they get it right, then quit.
# If they don't get it right, tell them if their next guess has to be higher or lower.
def problem4():
    randomNum = random.randint(0, 10)
    print(randomNum)
    userInput = ""
    while userInput != randomNum:
        userInput = int(input("Enter a number between 0 and 10\n"))
        if userInput < randomNum:
            print("guess higher")
        elif userInput > randomNum:
            print("guess lower")

if __name__ == '__main__':
    main()