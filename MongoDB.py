import pymongo
import config

# myclient = pymongo.MongoClient(mongodb+srv://mycluster-ptgp4.mongodb.net/MongoDB)

client = pymongo.MongoClient("mongodb+srv://"+config.username+":"+config.password+"@mycluster-ptgp4.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

# mongodb+srv://Elliot:<password>@mycluster-ptgp4.mongodb.net/test?retryWrites=true&w=majority