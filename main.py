import time
from termcolor import cprint
import lachpack

#Top-Level

#sets up the players
players = lachpack.setupPlayers()

#activates the game
lachpack.game(players)

#prints the score of each player
print("Results: ")
for i in range(0, len(players)):
  print("\n -", end="", flush=True)
  cprint(players[i].name, players[i].colour, end="", flush=True)
  print(": " + str(players[i].score))

#calculates the winners
winners, winids = lachpack.calculateWinner(players)

#prints the list of winners
print("\nWinner(s): ")
for i in range(0, len(winners)):
  pos = lachpack.binarySearch(players, winids[i])
  print("\n -", end="", flush=True)
  cprint(winners[i], players[pos].colour)
#Top-Level
