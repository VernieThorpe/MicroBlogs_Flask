import os
import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    client = MongoClient(os.environ.get("MONGODB_URI"))
    app.db=client.microblog


    @app.route("/", methods=["GET", "POST"])
    def home():

        if request.method =="POST":
            entry_content=request.form.get("content")
            entry_title=request.form.get("title")
            formatted_date=datetime.datetime.today().strftime("%d-%m-%Y")
            #entries.append((entry_content, formatted_date, entry_title))  
            app.db.entries.insert_one({"content": entry_content, "date": formatted_date, "title": entry_title})

        entries_with_date = [
            (
                entry["content"], 
                entry["date"],
                entry["title"], 
                datetime.datetime.strptime(entry["date"], "%d-%m-%Y").strftime("%b %d")
            )
            for entry in app.db.entries.find({})
        ]
        return render_template("home.html", entries=entries_with_date)
    
    return app