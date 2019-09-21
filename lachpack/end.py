def calculateWinner(players):
  maxScore = 0
  winners = []
  winids = []

  #searches list for the player with the highest score
  for i in range(len(players)):

    #if multiple players have the highest score, all are added as winners
    if players[i].score == maxScore:
      winners.append(players[i].name)
      winids.append(players[i].idnum)

    #if a new highest score is found, the old one is overwritten and all winners are removed from the win list
    elif players[i].score > maxScore:
      maxScore = players[i].score
      winners.clear()
      winids.clear()
      winners.append(players[i].name)
      winids.append(players[i].idnum)

  #returns the list of winners
  return winners, winids
