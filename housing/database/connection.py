## connection to MongoDB atlas for fetching data

from housing.constants import db_name,db_url
import pymongo

class connection_client:

    def __init__(self,db_name) :
        self.db_name = db_name
        self.url= db_url

        try:
            client = pymongo.MongoClient(self.url)
            db = client.test
            print('connection status : ',db)
            client.close()
            #return db
        except Exception as e:
            return e