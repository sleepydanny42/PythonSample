# This code is for The Guessing Game
# A user will input a number to guess the correct random number

print("Welcome to The Guessing Game!! Here, our lucky contestant will guess the correct random number!!")
name = input("What's going on new player!! What is your name? ")
print(name, ", good to have to on the show. Alright, you 5 tries to guess the correct number!"
            "The random number is in a range from 1 to 50.")

from random import randint
randomNum = randint(1, 50)

guess = int(input("Ok!, Make your first guess: "))

for i in range(4):
    if guess == randomNum:
        print("Congratulations!! You guessed the right number!!!")
    elif guess > randomNum:
        print("Your answer is too high. Try again.")
        guess = int(input("Choose another number: "))
    elif guess < randomNum:
        print("Your answer is too low. Try again.")
        guess = int(input("Choose another number: "))

print("Alright, you have used all your tries. The correct number was ", randomNum)

print("Thanks for playing The Guessing Game! See you next time!")