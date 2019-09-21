from termcolor import cprint
from .validate import oneNumValidate
from .validate import twoNumValidate
from .clear import clear
from .classes import player

def setupPlayers():
  colours = ["blue", "green", "red", "yellow"]
  players = []

  #gets the number of players for the game
  cprint("SCRABBLE SCORE TRACKER", "cyan", attrs=['bold'])
  x = str(input("How many players? \n >> "))
  x = int(twoNumValidate(x,"a number between 2 and 4, inclusive.",2,4))

  #gets the names of the players
  for i in range(x):

    clear()
    name = str(input("Please input the name of player " + str(i+1) + ". \n >> "))
    colour = str(input("Please input the colour of player " + str(i+1) + ", from blue, green, red, or yellow (no capitals). \n >> "))
    while not colour in colours:
      if not colour in colours:
        colour = str(input("Please choose from blue, green, red, or yellow, with no capitals. \n >> "))
    score = 0
    y = player(name, colour, score, i)
    players.append(y)

  #returns the list of players
  print("These are the players: \n")
  for i in range(len(players)):
      cprint(players[i].name, players[i].colour)
  return players
