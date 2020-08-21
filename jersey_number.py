# This program will ask for the name, height and weight of a player
# Once this is done, it will give the player a jersey number for the season

from random import randint

print("Welcome to the BrickBreakers basketball team! Here, you will enter in your information."
      "Once that is done, the jersey machine will issue a jersey number. Let's get started!")

roster = []

for i in range(11):
    jersey = randint(1, 50)
    name = input("What is your name? ")
    height = input("Now what is your height, in feet and inches? ")
    weight = int(input("Tell us your weight: "))
    print("Now that we have your information, your jersey number is ", jersey)
    roster.append([name, height, weight, jersey])

print("Here's the roster for the BrickBreakers:")
print(roster)
