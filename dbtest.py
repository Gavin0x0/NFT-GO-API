#!/usr/bin/python3
#%% 
import pymongo
 
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
 
dblist = myclient.list_database_names()
# dblist = myclient.database_names() 
print(dblist)
db = myclient["NFTGO"]
good = db.goods.find({"g_no":"1"})
print(good)