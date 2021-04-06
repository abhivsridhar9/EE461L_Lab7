from pymongo import MongoClient


def access_existing_db():
    cluster=MongoClient('mongodb+srv://asamant:UTEE461L@cluster1.oovet.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    db=cluster['api236']
    people_collection=db['people']

    for people in people_collection.find():
        print(people+'\n')

    cluster.close()

def create_new_db():
    cluster=MongoClient('mongodb+srv://asamant:UTEE461L@cluster1.oovet.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    db=cluster['as83788']
    people_collection=db['people']
    # people_dit=ct = {"First Name": "Steve", "description": description, "id": ProjectManagement.id}


access_existing_db()