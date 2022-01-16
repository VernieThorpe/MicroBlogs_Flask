import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

entries = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method =="POST":
        entry_content=request.form.get("content")
        entry_title=request.form.get("title")
        formatted_date=datetime.datetime.today().strftime("%d-%m-%Y")
        entries.append((entry_content, formatted_date, entry_title))

        entries_with_date = [
            (
                entry[0], 
                entry[1],
                entry[2], 
                datetime.datetime.strptime(entry[1], "%d-%m-%Y").strftime("%b %d")
            )
            for entry in entries
        ]
    return render_template("home.html", entries=entries_with_date)
