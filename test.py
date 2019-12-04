import pymongo
import auth

MONGODB_URI = 'mongodb+srv://'+auth.username+':'+auth.password+'@mycluster-ptgp4.mongodb.net/test?retryWrites=true&w=majority'
DBS_NAME = "task_manager"
COLLECTION_NAME = "tasks"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected.")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not establish connection: {0}").format(e)


def get_record():
    try:
        doc = coll.find()
        for record in doc:
            print(record)
    except:
        print("Error accessing the database.")
    

conn = mongo_connect(MONGODB_URI)
db = conn[DBS_NAME]
coll = db[COLLECTION_NAME]

get_record()

