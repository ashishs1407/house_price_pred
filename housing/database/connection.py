## connection to MongoDB atlas for fetching data

from housing.constants import db_name,db_url
import pymongo

class connection_client:

    def __init__(self,database_name=db_name) :
        self.database_name = db_name
        self.url= db_url

        try:
            self.client = pymongo.MongoClient(self.url)
            self.db = self.client.test
            #print('connection status : ',db)
            #db = client[database_name]
            print(self.db)
            #print("Collections are : ",db.list_database_names())
            
            self.client.close()
        except Exception as e:
            raise e