import pymongo
import json

conn = pymongo.MongoClient("mongodb://192.168.0.15:27017/")


#####4.1
# db = conn.example
#db.collection_names()
#widgets = db.widgets
#widgets.insert({"foo":"bar"})

#widgets.insert({"name": "flibnip", "description": "grade-A industrial flibnip", "quantity": 3})

# doc = db.widgets.find_one({"name": "flibnip"})
# doc['quantity'] = 4
# db.widgets.save(doc)

# for doc in widgets.find():
#     print doc
#     del doc['_id']
#     print json.dumps(doc)
# print db.collection_names()
# print widgets.find_one({"name": "flibnip"})

####4.2
db = conn.example2
db.words.insert({"word": "oarlock", "definition": "A device attached to a rowboat to hold the oars in place"})
db.words.insert({"word": "seminomadic", "definition": "Only partially nomadic"})
db.words.insert({"word": "perturb", "definition": "Bother, unsettle, modify"})
