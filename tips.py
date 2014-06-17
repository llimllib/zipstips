import json
import random

from flask import Flask, render_template

app = Flask(__name__)

TIPS = json.load(file("parse/tips.json"))
TIPDATES = dict((tip["dt"], tip) for tip in TIPS)

@app.route('/')
def tip():
    tip = random.choice(TIPS)
    large = False
    if len(tip["tiptxt"].split()) > 200:
        large = True
    return render_template("zip.html", tip=tip, large=large)

@app.route('/<month>/<day>/<year>')
def permatip(month, day, year):
    tip = TIPDATES["{}/{}/{}".format(month, day, year)]
    large = False
    if len(tip["tiptxt"].split()) > 250:
        large = True
    return render_template("zip.html", tip=tip, large=large)

if __name__ == '__main__':
    app.debug = True
    app.run()
