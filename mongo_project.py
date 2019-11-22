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

def show_menu():
    print("")
    print("1. Add a record.")
    print("2. Find a rcord by name.")
    print("3. Edit a record.")
    print("4. Delete a record.")
    print("5. Exit.")

    option = input("Enter option: ")
    return option


