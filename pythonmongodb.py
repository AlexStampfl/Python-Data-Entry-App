# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 10:05:44 2022

@author: alexs
"""
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017')
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# print(myclient.list_database_names())

# def checkDataBase():
#     dbList = myclient.list_database_names()
#     if "mydatabase" in dbList:
#         print("The database exists.")
#     print(mydb.list_collection_names())
#     collist = mydb.list_collection_names()
#     if "customers" in collist:
#         print("The collection exists.")
        
# checkDataBase()

# def idManually():
#     mydict = {"name": "John", "address":"Highway 37"}
#     x = mycol.insert_one(mydict)
#     print(x.inserted_id)
    
# # idManually()

# def myList():
myList = [
   	{ "_id": 1, "name": "John", "address": "Highway 37"},
   	{ "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
   	{ "_id": 3, "name": "Amy", "address": "Apple st 652"},
   	{ "_id": 4, "name": "Hannah", "address": "Mountain 21"},
   	{ "_id": 5, "name": "Michael", "address": "Valley 345"},
   	{ "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
   	{ "_id": 7, "name": "Betty", "address": "Green Grass 1"},
   	{ "_id": 8, "name": "Richard", "address": "Sky st 331"},
   	{ "_id": 9, "name": "Susan", "address": "One way 98"},
   	{ "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
   	{ "_id": 11, "name": "Ben", "address": "Park Lane 38"},
   	{ "_id": 12, "name": "William", "address": "Central st 954"},
   	{ "_id": 13, "name": "Chuck", "address": "Main Road 989"},
   	{ "_id": 14, "name": "Viola", "address": "Sideway 1633"}
 	]
    
# myList()

# def insertMany(myList):
x = mycol.insert_many(myList)
# print(x.inserted_ids)
    
# insertMany(myList)

# def findOne():
#     x = mycol.find_one()
#     print(x)
    
# # findOne()
    
# def findAll():
#     for x in mycol.find():
#         print(x)
        
# # findAll()

# def findSome():
#     for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1}):
#         print(x)
        
# # findSome()

# def excludeAddress():
#     for x in mycol.find({},{ "address": 0}):
#         print(x)
        
# # excludeAddress()

# def queryObjection():
#     myquery = {"address": "Park Lane 38"}
#     mydoc = mycol.find(myquery)
#     for x in mydoc:
#         print(x)
        
# # queryObjection()

# def advancedQuery():
#     myquery = { "address": { "$gt": "S" } }
#     mydoc = mycol.find(myquery)
#     for x in mydoc:
#         print(x)
        
# # advancedQuery()

# def regularExpressions():
#     myquery = { "address": { "$regex": "^S"} }
#     mydoc = mycol.find(myquery)
#     for x in mydoc:
#         print(x)
    
# # regularExpressions()

# def sortFunction():
#     mydoc = mycol.find().sort("name")
#     for x in mydoc:
#         print(x)
    
# # sortFunction()

# def sortDescending():
#     mydoc = mycol.find().sort("name", -1)
#     for x in mydoc:
#         print(x)

# # sortDescending()

# def deleteDocument():
#     myquery = { "address": "Mountain 21" }
#     mycol.delete_one(myquery)

# # deleteDocument()

# def deleteManyDoc():
#     myquery = { "address": {"$regex": "^S"} }
#     x = mycol.delete_many(myquery)
#     print(x.deleted_count, " documents deleted.")

# # deleteManyDoc()

# def deleteCollection():
#     x = mycol.delete_many({})
#     print(x.deleted_count, " documents deleted")

# deleteCollection()












    
    
    
    
    
    
