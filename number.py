# Ibrahim Mansour
# import from random
import random
print("Welcome to a Number Guessing Game")
print("To start you have to enter the range of numbers you want to play")
# input range
n = input("Enter the lowest number: ")
n = int(n)
m = input("Enter the highest number: ")
m = int(m)
num = random.randint(n,m)
# input amount of tries, checking if input is integer
attempt = input("How many attempt do you want to have?: ")
attempt = int(attempt)
message = "You lost"
while attempt >0:
    ChoosingNumber = input("Enter Number: ")
    ChoosingNumber = int(ChoosingNumber)
    if ChoosingNumber == num:
        message = "You won"
        print(message)
        break
    else:
        if ChoosingNumber > num:
            print("Your guessed it too high")
        else:
            print("Your guess is too low")
            attempt -= 1
    if attempt == 0:
        print("You have no more chances left")
        print(message)
        print("The guessing number was: ", num)
    else:
        print("Try again! You have", attempt, "attempts left")