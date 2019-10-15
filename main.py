#!/usr/bin/env python3
from flask import Flask, render_template, request
import lachpack

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    global i,setupDone
    setupDone = False
    i = 1
    return render_template("index.html")

@app.route("/setup", methods=["POST"])
def setup():
    global i,setupDone,players
    x = int(request.form["number"])
    if setupDone == True:
        lachpack.doSetup(players, i)
        i += 1
    if i > x:
        loop = True
        global scoreInputs,inputTypes,colours
        scoreInputs = []
        inputTypes = []
        colours = []
        for i in range(4):
            if i <= len(players)-1:
                scoreInputs.append(players[i].name)
                inputTypes.append("number")
                colours.append(players[i].colour)
            else:
                scoreInputs.append("")
                inputTypes.append("hidden")
                colours.append("white")
        return render_template("gameRound.html", loop=loop, input1=scoreInputs[0], input2=scoreInputs[1], input3=scoreInputs[2], input4=scoreInputs[3], type1=inputTypes[0], type2=inputTypes[1], type3=inputTypes[2], type4=inputTypes[3], colour1=colours[0], colour2=colours[1], colour3=colours[2], colour4=colours[3])
    else:
        setupDone = True
        return render_template("playerSetup.html", i=i, x=str(x))

@app.route("/game", methods=["POST"])
def game():
    global scoreInputs,inputTypes,colours,players
    loop = request.form["loop"]
    continueLoop = request.form["continue"]
    for i in range(len(players)):
        players[i].score = players[i].score + int(request.form[players[i].name])
    if continueLoop == True:
        return render_template("gameRound.html", loop=loop, input1=scoreInputs[0], input2=scoreInputs[1], input3=scoreInputs[2], input4=scoreInputs[3], type1=inputTypes[0], type2=inputTypes[1], type3=inputTypes[2], type4=inputTypes[3], colour1=colours[0], colour2=colours[1], colour3=colours[2], colour4=colours[3])
    else:
        loop = False
        return render_template("negativeRound.html", loop=loop, input1=scoreInputs[0], input2=scoreInputs[1], input3=scoreInputs[2], input4=scoreInputs[3], type1=inputTypes[0], type2=inputTypes[1], type3=inputTypes[2], type4=inputTypes[3], colour1=colours[0], colour2=colours[1], colour3=colours[2], colour4=colours[3])

@app.route("/end", methods=["POST"])
def end():
    global inputTypes,colours,players
    for i in range(len(players)):
        players[i].score = players[i].score - int(request.form[players[i].name])
    players,winners,winscores = lachpack.calculateWinner(players)
    listPlayers = []
    listScores = []
    winColours = []
    winnerScores = []
    listWinners = []

    for i in range(4):
        if i <= len(players)-1:
            listPlayers.append(players[i].name + ": ")
            listScores.append(str(players[i].score))
        else:
            listPlayers.append("")
            listScores.append("")

        if i <= len(winners)-1:
            pos = lachpack.linearSearch(players, winners[i])
            listWinners.append(players[pos].name + ": ")
            winnerScores.append(str(players[pos].score))
            winColours.append(players[pos].colour)
        else:
            listWinners.append("")
            winnerScores.append("")
            winColours.append("")

    return render_template("end.html", player1=listPlayers[0], player2=listPlayers[1], player3=listPlayers[2], player4=listPlayers[3], score1=listScores[0], score2=listScores[1], score3=listScores[2], score4=listScores[3], colour1=colours[0], colour2=colours[1], colour3=colours[2], colour4=colours[3], winner1=listWinners[0], winner2=listWinners[1], winner3=listWinners[2], winner4=listWinners[3], wscore1=winnerScores[0], wscore2=winnerScores[1], wscore3=winnerScores[2], wscore4=winnerScores[3], wcolour1=winColours[0], wcolour2=winColours[1], wcolour3=winColours[2], wcolour4=winColours[3])


if __name__ == "__main__":
    players = []
    app.run(host = "localhost", port = 3000)
