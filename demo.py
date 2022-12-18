from housing.constants import db_name, db_url
from housing.database import connection
import os



if __name__ == "__main__":
    client = connection.connection_client(db_name)
    
    
