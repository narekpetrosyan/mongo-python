from .mongo import _Mongo

class Operations(_Mongo):
    def __init__(self):
        super().__init__()
        self.__mclient = self.get_client()


    def get_db_names(self):
        return self.__mclient.list_database_names()


    def get_db_by_name(self, name: str):
        return self.__mclient[name]


    def insert_doc(self, collection, obj, many=False):
        if not many:
            inserted_one_doc = collection.insert_one(obj)
            return inserted_one_doc.inserted_id

        if type(obj) == list:
            inserted_docs = collection.insert_many(obj)
            return inserted_docs.inserted_ids
        else:
            raise Exception("Obj type must be list")


    def count_docs(self, collection):
        count = collection.count_documents(filter={})
        return count


    def find_all(self, collection):
        found_docs = collection.find()
        return found_docs
        

    def find_by_id(self, collection, id):
        _id = _Mongo.toObjectId(id)
        found_doc = collection.find_one({"_id": _id})
        return found_doc

