from dotenv import find_dotenv, load_dotenv
import pprint
from mongo.operations import Operations

load_dotenv(find_dotenv())

printer = pprint.PrettyPrinter()

operations = Operations()
database = operations.get_db_by_name('pymongo')


collection = database.test

# def insert_doc():
#     collection = database.test
#     docs = []
#     doc = {
#         "name": "Narek",
#         "type": "Test"
#     }
#     docs.append(doc)
#     inserted = operations.insert_doc(collection,docs,True)
#     printer.pprint(inserted)


# insert_doc()


# def find_all_docs():
#     collection = database.test
#     found = operations.find_all(collection)
#     for item in found:
#         printer.pprint(item)


# find_all_docs()

# printer.pprint(operations.count_docs(collection))
# printer.pprint(operations.find_by_id(collection, '62bf33b8085a4554c0b67ce2'))
printer.pprint(operations.find_by_id(collection, '62bf33b8085a4554c0b67ce2'))