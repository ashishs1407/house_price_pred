from housing.constants import db_name, db_url
from housing.database import connection
import os



if __name__ == "__main__":
    conn = connection.connection_client()
    print("databases are as 123 : " ,conn.client[db_name])
    print("databases are as 456: " ,conn)
    
    
