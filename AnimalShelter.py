# Trent Hesler - CS340-11221-M01
# Assignment prompt:
# Develop a CRUD class that, when instantiated, provides the following functionality:
#     A method that inserts a document into a specified MongoDB database and collection
#         Input argument to function will be a set of key/value pairs in the data type acceptable to the MongoDB driver insert API call
#         Return “True” if successful insert, else “False”
#     A method that queries for documents from a specified MongoDB database and collection
#         Input arguments to function should be the key/value lookup pair to use with the MongoDB driver find API call
#         Return result in a list if the command is successful, else an empty list..
#     Important: Be sure to use find() instead of find_one() when developing your method. Hint: You must work with the MongoDB cursor returned by the find() method.

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,USER,PASS,HOST,PORT,DB,COL):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        # USER = 'aacuser'
        # PASS = 'SNHU2024'
        # HOST = 'nv-desktop-services.apporto.com'
        # PORT = 30109
        # DB = 'AAC'
        # COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        # If something got passed in, try to insert it
        if data is not None:
             try:
                 if ( self.database.animals.insert_one(data) ) != 0 :
                     # If insertion succeeds, return true
                     return True
                 else:
                     # If insertion fails, return false
                     return False
            # If the input exists but is invalid, display an error message and return false
             except Exception as e:
                  print({e.__class__.__name__})
                  return False
        else:
            # If there is no input, display an error message
            raise Exception("Nothing to save, because data parameter is empty")
        return False
        

# Create method to implement the R in CRUD.
    def read(self,query=None):
        # Make sure a query got passed in
        if query is not None:
            # If the query isn't empty, try to search for it
            try:
                result = list(self.database.animals.find(query,{'_id':False}))
            # If the query exists, but is invalid, catch the exception, display an error message,
            # and return an empty list
            except Exception as e:
                print({e.__class__.__name__})
                result = list()
        else:
            # If the query is empty, return an empty list
            result = list()
        return result

# Create a method to implement the U in CRUD
    def update(self,query=None,replacement=None):
        # Make sure something was passed in
        if (query is not None) and (replacement is not None):
            # If query and replacement have content, try update op
            try:
                dbupdate = self.database.animals.update_many(query,replacement)
                return dbupdate.modified_count
            # Catch invalid queries or replacements
            except Exception as e:
                print({e.__class__.__name__})
        # If there is no valid input, return 0
        return 0

# Create a method to implement the D in CRUD
    def remove(self,query=None):
        #Make sure a query was provided
        if query is not None:
            # Make sure the query is valid
            try:
                dbdel = self.database.animals.delete_many(query)
                # Return number of deletes
                return dbdel.deleted_count
            # Catch invalid queries
            except Exception as e:
                print(e.__class__.__name__)
        # If nothing was deleted, return 0
        return 0
