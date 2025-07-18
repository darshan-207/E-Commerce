from pymongo import MongoClient
import bcrypt

client = MongoClient('mongodb://localhost:27017/')
db = client['nerd']
users = db['users']

users.insert_one({'username': 'admin', 'password': 'pass', 'role': 'admin'})


users.insert_one({'username': 'darshan', 'password': 'pass', 'role': 'user'})

print("Users inserted successfully")
