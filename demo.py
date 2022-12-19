from housing.constants import db_name, db_url
from housing.database import connection
from housing.logger.housing_logger import logging
from housing.exception.housing_exception import HousingException
import sys,os



if __name__ == "__main__":
    try :
        logging.info("connecting to mongoDB")
        conn = connection.connection_client()
        print("databases are as 123 : " ,conn.client[db_name])
        print("databases are as 456: " ,conn)
    except Exception as e:
        raise HousingException(e,sys)
    
    
