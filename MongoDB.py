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
db = conn[DBS_NAME]
coll = db[COLLECTION_NAME]
print("Collection found")
print(coll)

test_record = {
    "test" : "success"
}

first_record = {
    'first': 'john',
    'last': 'lennon',
    'dob': '09/10/1940',
    'gender': 'm',
    'hair_colour': 'brown',
    'occupation': 'beatle',
    'nationality': 'english'
}

coll.insert_one(test_record)
# print("Record inserted")

# documents = coll.find()
# print(documents)

for doc in coll.find():
    print(doc)
print("docs printed")