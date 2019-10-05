#!/usr/bin/env python3
import time
from termcolor import cprint

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")
