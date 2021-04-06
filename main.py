import datetime
from pymongo import MongoClient

# method to access an existing db and read from people connection
def access_existing_db():
    # connect to the provided cluster
    cluster = MongoClient(
        'mongodb+srv://asamant:UTEE461L@cluster1.oovet.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

    # access the database api236
    db = cluster['api236']

    # access the collection people
    people_collection = db['people']

    # print all the entries stored in the people collection
    for people in people_collection.find():
        print(people)

    # close connection to cluster
    cluster.close()


# method to create a new database, new collection, and add a person entry to that new collection
def create_new_db():
    # connect to the provided cluster
    cluster = MongoClient('mongodb+srv://asamant:UTEE461L@cluster1.oovet.mongodb.net/myFirstDatabase?retryWrites=true&w'
                          '=majority')

    # create a new database in the cluster
    db = cluster['as83788']

    # create a new collection in the database
    people_collection = db['people']

    # create a new person entry to then put into the newly created collection
    name_dict = {'first': 'Steve', 'last': 'Jobs'}
    contribution_list = ['Mac Computer', 'iPhone', 'iPad']
    birth = datetime.datetime(1955, 2, 24)
    death = datetime.datetime(2011, 10, 5)

    # entry is compiled in the form of a dictionary object
    people_dict = {'name': name_dict, 'birth':birth,'death':death,'contribs': contribution_list, 'views': 1250000}

    #  add new entry to the collection
    people_collection.insert_one(people_dict)

    # print out all entries in the collection
    for people in people_collection.find():
        print(people)

    # close connection to cluster
    cluster.close()

# cal method to read from an existing database
access_existing_db()

# call method to create new database and add to it
create_new_db()
