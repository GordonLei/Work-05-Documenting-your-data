import pymongo, json
with open("movies.json", "r") as f:
    moviesList = json.load(f)

connection = pymongo.MongoClient("homer.stuy.edu")
db = connection.leiGkalmakovaB 
collection = db.movies
collection.insert_many(moviesList) 

movies