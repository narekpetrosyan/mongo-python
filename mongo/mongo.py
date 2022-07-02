"""MongoDB module."""
import os
from pymongo import MongoClient
from bson.objectid import ObjectId


class _Mongo:
    def __init__(self):
        try:
            db_user = os.environ.get("MONGO_USER")
            db_password = os.environ.get("MONGO_PASSWORD")
            self.__connection_url = f"""mongodb+srv://{db_user}:{db_password}@cluster0.debap.mongodb.net/?retryWrites=true&w=majority"""
            self.set_client()
        except OSError as err:
            print(f"{type(err)} <=====> error = {err}")
            raise err

    def set_client(self):
        self.__client = MongoClient(self.__connection_url)

    def get_client(self):
        return self.__client

    # static method
    @staticmethod
    def to_object_id(id):
        return ObjectId(id)
