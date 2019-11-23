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

def get_record():
    print("")
    first = input("Enter first name:    ")
    last = input("Enter last name:     ")

def add_record():
    print("")
    first = input("Enter first name:    ")
    last = input("Enter last name:     ")
    dob = input("Enter date of birth:   ")
    gender = input("Enter gender:   ")
    hair_colour = input("Enter hair colour: ")
    occupation = input("Enter occupation:   ")
    nationality = input("Enter nationality:     ")

    new_doc = {"first": first.lower(), "last":last.lower(), "dob":dob, "gender":gender, "hair_colour":hair_colour, "occupation":occupation, "nationality":nationality}

    try:
        coll.insert(new_doc)
        print("")
        print("Document inserted.")
    except:
        print("Error accessing the database.")



def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        if option == "2":
            print("You have selected option 2")
        if option == "3":
            print("You have selected option 3")
        if option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")

conn = mongo_connect(MONGODB_URI)
db = conn[DBS_NAME]
coll = db[COLLECTION_NAME]

main_loop()

