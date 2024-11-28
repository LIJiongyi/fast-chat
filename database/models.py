from pymongo import MongoClient
from datetime import datetime

# 连接到 MongoDB
client = MongoClient("mongodb://localhost:27017/")

# 选择数据库
db = client["yourdbname"]

# 定义用户集合
class User:
    collection = db["users"]

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save(self):
        User.collection.insert_one(self.__dict__)

    @staticmethod
    def find_by_username(username):
        return User.collection.find_one({"username": username})

# 定义联系人集合
class Contact:
    collection = db["contacts"]

    def __init__(self, user_id, contact_id):
        self.user_id = user_id
        self.contact_id = contact_id

    def save(self):
        Contact.collection.insert_one(self.__dict__)

    @staticmethod
    def find_by_user_id(user_id):
        return Contact.collection.find({"user_id": user_id})

# 定义消息集合
class Message:
    collection = db["messages"]

    def __init__(self, sender_id, receiver_id, content):
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.content = content
        self.timestamp = datetime.utcnow()

    def save(self):
        Message.collection.insert_one(self.__dict__)

    @staticmethod
    def find_by_sender_id(sender_id):
        return Message.collection.find({"sender_id": sender_id})

    @staticmethod
    def find_by_receiver_id(receiver_id):
        return Message.collection.find({"receiver_id": receiver_id})