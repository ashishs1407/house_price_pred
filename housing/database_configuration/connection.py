## connection to MongoDB atlas for fetching data

from housing.constants.regular import DB_NAME,DB_URL
from housing.exception.housing_exception import HousingException
import pymongo
import os,sys

class ConnectionClient:

    def __init__(self,database_name=DB_NAME)-> None :
        self.database_name = DB_NAME
        #self.url : str = DB_URL
        self.url : str = os.environ.get('DB_URL')

        try:
            self.client = pymongo.MongoClient(self.url)
            self.db = self.client.test
            if self.db is None :
                print("connection failed")
            else:
                
                print("List of Databases : ",self.client.list_database_names())
                print('connection established succesfully')
            
    
            #self.client.close()
        except Exception as e:
            raise HousingException(e,sys)