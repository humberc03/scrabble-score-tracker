import replit
import time
from termcolor import cprint

#Classes
class player():
  def __init__(self, name, colour, score):
    self.name = name
    self.colour = colour
    self.score = score
#Classes

#Validation
def subValidateStart(extender):

  #receives a new input from the user
  replit.clear()
  print("You must input " + extender)
  x = input("\n >> ")

  #returns the new input
  return x

def oneNumValidate(x,extender,numOne):

  #ensures the input is a number within range
  if any(c.isalpha() for c in x) == True:
    x = oneNumSubValidate(x,extender,numOne)
  if int(x) < numOne:
      x = oneNumSubValidate(x,extender,numOne)
 
  #returns the validated input
  return x

def oneNumSubValidate(x,extender,numOne):
  
  #gets new input
  x = subValidateStart(extender)
  return oneNumValidate(x,extender,numOne)

def twoNumValidate(x,extender,numOne,numTwo):
  
  #ensures the input is a number within range
  if any(c.isalpha() for c in x) == True:
    x = twoNumSubValidate(x,extender,numOne,numTwo)
  if int(x) < numOne or int(x) > numTwo:
      x = twoNumSubValidate(x,extender,numOne,numTwo)
  
  #returns the validated input
  return x

def twoNumSubValidate(x,extender,numOne,numTwo):
  
  #gets new input
  x = subValidateStart(extender)
  return twoNumValidate(x,extender,numOne,numTwo)
#Validation

#End
def calculateWinner(players):
  maxScore = 0
  winners = []

  #searches list for the player with the highest score
  for i in range(len(players)):

    #if multiple players have the highest score, all are added as winners
    if players[i].score == maxScore:
      winners.append(players[i].name)

    #if a new highest score is found, the old one is overwritten and all winners are removed from the win list
    elif players[i].score > maxScore:
      maxScore = players[i].score
      winners.clear()
      winners.append(players[i].name)

  #returns the list of winners
  return winners
#End

#Setup
def setupPlayers():
  colours = ["blue", "green", "red", "yellow"]
  players = []

  #gets the number of players for the game
  cprint("SCRABBLE SCORE TRACKER", "cyan", attrs=['bold'])
  x = str(input("How many players? \n >> "))
  x = int(oneNumValidate(x,"a number that is at least 2.",2))

  #gets the names of the players
  for i in range(x):

    name = str(input("Please input the name of player " + str(i+1) + ". \n >> "))
    colour = str(input("Please input the colour of player " + str(i+1) + ", from blue, green, red, or yellow (no capitals). \n >> "))
    while not colour in colours:
      if not colour in colours:
        colour = str(input("Please choose from blue, green, red, or yellow, with no capitals. \n >> "))
    score = 0
    y = player(name, colour, score)
    players.append(y)

  #returns the list of players
  print("These are the players: \n")
  for i in range(len(players)):
      cprint(players[i].name, players[i].colour)
  return players
#Setup

#Game
def gameRound(players, extender):

  #clears the console output and list of scores
  roundScores = []

  #gets the scores for each player
  for i in range(0, len(players)):
    print("\nPlayer: ", end="", flush=True)
    cprint(players[i].name, players[i].colour)
    x = input(extender + " \n >> ")
    x = int(oneNumValidate(x,"an integer.",-100))
    roundScores.append(x)

  #returns the scores for this round
  time.sleep(2)
  return roundScores

def game(players):

  #activates game and sets up a list for the total scores
  x = True
  totalScores = [0]*len(players)

  #runs until there are no more rounds
  while x == True:

    #gets the scores for the new round
    roundScores = gameRound(players, "Enter the score for this round.")

    #updates the total score for each player
    for i in range(0, len(players)):
      players[i].score = players[i].score + roundScores[i]
      print(players[i].name,players[i].score)

    #determines if there is to be another round of play
    y = input("Continue to another round? \n 1. Yes \n 2. No \n >> ")
    y = int(twoNumValidate(y,"either 1 or 2.",1,2))

    #continues or ends the game, depending on input
    if y == 1:
      x = True
    if y == 2:
      x = False

      #determines the score to be removed from each player's total
      roundScores = gameRound(players, "Enter, as positives, the scores to be taken away due to remaining letters (enter 0 if no remaining letters).")

      #updates each player's total
      for i in range(0, len(players)):
        print(players[i].score)
        players[i].score = players[i].score - roundScores[i]
        print(players[i].score)

      #returns the list of total scores at the end of the game
      return totalScores
#Game

#Top-Level

#sets up the players
players = setupPlayers()

#activates the game
game(players)

#prints the score of each player
print("Results: ")
for i in range(0, len(players)):
  print("\n -" + players[i].name + ": " + str(players[i].score))

#calculates the winners
winners = calculateWinner(players)

#prints the list of winners
print("\nWinner(s): ")
for i in range(0, len(winners)):
  print("\n -" + winners[i])
#Top-Level
