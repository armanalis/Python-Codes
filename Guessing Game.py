#The purpose of this code that we want to user guess the number and
#we should find the number that asks the user high or low that
#I guessed number is and eventually find the number that user guessed
import random

num = int(input("Enter a number that I will guess:"))
guess_num = 50

while num != guess_num:
    print("My guess is", guess_num)
    choice = input("Is it too high or low?")
    if choice == 'High':
        guess_num -= random.randint(1, 4)

    elif choice == 'Low':
        guess_num += random.randint(1, 4)

    else:
        print("Invalid input")
print("Your guessed number is:", num)

