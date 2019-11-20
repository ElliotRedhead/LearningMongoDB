import pymongo
import config

MONGODB_URI = 'mongodb+srv://'+config.username+':'+config.password+'@mycluster-ptgp4.mongodb.net/test?retryWrites=true&w=majority'
DBS_NAME = "TestDB"
COLLECTION_NAME = "TestMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected.")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not establish connection: {0}").format(e)

conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

documents = coll.find()

for doc in documents:
    print(doc)