import time
from termcolor import cprint
from .validate import oneNumValidate
from .validate import twoNumValidate
from .clear import clear

def gameRound(players, extender):

  #clears the console output and list of scores
  roundScores = []
  clear()

  #gets the scores for each player
  for i in range(0, len(players)):
    print("\nPlayer: ", end="", flush=True)
    cprint(players[i].name, players[i].colour)
    x = input(extender + " \n >> ")
    x = int(oneNumValidate(x,"an integer.",-100))
    roundScores.append(x)

  #returns the scores for this round
  time.sleep(1)
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

    #determines if there is to be another round of play
    clear()
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
        players[i].score = players[i].score - roundScores[i]

      #returns the list of total scores at the end of the game
      return totalScores
