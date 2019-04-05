import psycopg2
from psycopg2 import pool


connection_pool = pool.SimpleConnectionPool(5, 10, 
                                                    user='danielgriffin', 
                                                    password='', 
                                                    database='learning', 
                                                    host='localhost')

class ConnectionFromPool:
    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = connection_pool.getconn()
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        connection_pool.putconn(self.connection)









def connect():
    return psycopg2.connect(user='danielgriffin', password='', 
                            database='learning', host='localhost')








create_users_table_sql = '''CREATE TABLE users 
                            (
                                id SERIAL PRIMARY KEY,
                                email character varying(255),
                                first_name character varying(255),
                                last_name character varying(255)
                            )'''