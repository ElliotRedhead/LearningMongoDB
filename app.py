import os
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = "task_manager"
app.config["MONGO_URI"] = "mongodb+srv://"config.username":"config.password"@mycluster-ptgp4.mongodb.net/test?retryWrites=true&w=majority"

@app.route("/")
def hello():
    return "Hello world... again."

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=os.environ.get("PORT"),
        debug=True)