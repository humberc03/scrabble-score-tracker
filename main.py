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
    global i,setupDone
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
    global scoreInputs,inputTypes,colours
    loop = request.form["loop"]
    for i in range(len(players)):
        players[i].score = players[i].score + request.form[players[i].name]
    continueLoop = request.form["continue"]
    if continueLoop == True:
        return render_template("gameRound.html", loop=loop, input1=scoreInputs[0], input2=scoreInputs[1], input3=scoreInputs[2], input4=scoreInputs[3], type1=inputTypes[0], type2=inputTypes[1], type3=inputTypes[2], type4=inputTypes[3], colour1=colours[0], colour2=colours[1], colour3=colours[2], colour4=colours[3])
    else:
        return render_template("gameRound.html", loop=loop, input1=scoreInputs[0], input2=scoreInputs[1], input3=scoreInputs[2], input4=scoreInputs[3], type1=inputTypes[0], type2=inputTypes[1], type3=inputTypes[2], type4=inputTypes[3])

if __name__ == "__main__":
    players = []
    app.run(host = "localhost", port = 3000)
