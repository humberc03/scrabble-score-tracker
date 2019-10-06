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
        end = "we did it"
        return render_template("doneanddone.html", end=end)
    else:
        setupDone = True
        return render_template("playerSetup.html", i=i, x=str(x))

if __name__ == "__main__":
    players = []
    app.run(host = "localhost", port = 3000)
