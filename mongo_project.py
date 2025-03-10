import pymongo
import os
from os import path
if path.exists("auth.py"):
  import auth

username = os.environ.get("username")
password = os.environ.get("password")

MONGODB_URI = 'mongodb+srv://'+username+':'+password+'@mycluster-ptgp4.mongodb.net/test?retryWrites=true&w=majority'
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
    print("2. Find a record by name.")
    print("3. Edit a record.")
    print("4. Delete a record.")
    print("5. Exit.")

    option = input("Enter option: ")
    return option

def get_record():
    print("")
    first = input("Enter first name:    ")
    last = input("Enter last name:     ")
    try:
        doc = coll.find_one({"first":first.lower(), "last": last.lower()})
    except:
        print("Error accessing the database.")
    if not doc:
        print("")
        print("Error. No results found.")
    return doc

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

def find_record():
    doc = get_record()
    if doc:
        print("")
        for key, value in doc.items():
            if key !="_id":
                print(key.capitalize()+": " + value.capitalize())

def edit_record():
    doc = get_record()
    if doc:
        update_doc={}
        print("")
        for key, value in doc.items():
            if key != "_id":
                update_doc[key] = input(key.capitalize() + " [" + value + "] = ")

                if update_doc == "":
                    update_doc = value
        try:
            coll.update_one(doc, {"$set": update_doc})
            print("")
            print("Document updated.")
        except:
            print("Error accessing the database.")

def delete_record():
    doc = get_record()
    if doc:
        print("")
        for key, value in doc.items():
            if key != "_id":
                print(key.capitalize() + ": " + value.capitalize())
        print("")
        confirmation = input("Is this the document you would like to delete?\nY or N?")
        print("")

        if confirmation.lower() == "y":
            try:
                coll.remove(doc)
                print("Document deleted.")
            except:
                print("Error accesing the database.")
        else:
            print("Document not deleted.")




def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        if option == "2":
            find_record()
        if option == "3":
            edit_record()
        if option == "4":
            delete_record()
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

