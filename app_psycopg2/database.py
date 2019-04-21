import psycopg2
from psycopg2 import pool


connection_pool = pool.SimpleConnectionPool(5, 10, 
                                                    user='danielgriffin', 
                                                    password='', 
                                                    database='learning', 
                                                    host='localhost')

class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = connection_pool.getconn()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
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