# This will help users to put list together of the favorite NBA players
# The user will also input the jersey numbers of these players

print("Good morning! Welcome to the ESPN Favorite Players app!")
print("Here, you will be able to input for your 10 favorite players into lists!. It can be"
      "based on position, teams, best scorers, whatever you see fit.")
name = input("Before we begin, let us first get your name: ")
print("Well good day to you " + name + ". Now let's begin!")

players = []

for x in range(10):
      p_name = input("Now, who is one of your favorite players: ")
      players.insert(x, p_name)

print("Ok " + name + ", here is your list of favorite players!")
print(players)

print("Ok " + name + ", now give use the jersey number of these players")
jersey = []

for i in range(10):
      p_jersey = int(input("Give us a jersey number: "))
      jersey.insert(i, p_jersey)

print("Now, here's the updated lists of your favorite players and their jersey numbers!")
print(players)
print(jersey)