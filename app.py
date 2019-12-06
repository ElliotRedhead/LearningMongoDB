import os
import auth
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
MONGODB_URI = 'mongodb+srv://'+auth.username+':'+auth.password+'@mycluster-ptgp4.mongodb.net/test?retryWrites=true&w=majority'
DBS_NAME = "task_manager"
COLLECTION_NAME = "tasks"

app.config["MONGO_DBNAME"] = "task_manager"
app.config["MONGO_URI"] = "mongodb+srv://"+auth.username+":"+auth.password+"@mycluster-ptgp4.mongodb.net/task_manager?retryWrites=true&w=majority"


mongo = PyMongo(app)
test_dict = {"insertionTest":"true"}

@app.route("/")
@app.route("/get_tasks")
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find(), test=mongo.db.collection.count())

@app.route("/add_task")
def add_task():
    return render_template("addtask.html",
    categories=mongo.db.categories.find())

@app.route("/insert_task", methods=["POST"])
def insert_task():
    tasks = mongo.db.tasks
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for("get_tasks"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP","127.0.0.1"),
        port=os.environ.get("PORT","5000"),
        debug=True)
