import psycopg2
from psycopg2 import pool


class Database:
    __connection_pool = None


    @classmethod
    def initialize(cls):
        cls.__connection_pool = pool.SimpleConnectionPool(1, 10, 
                                                    user='danielgriffin', 
                                                    password='', 
                                                    database='learning', 
                                                    host='localhost')

    @classmethod
    def get_connection(cls):
        return cls.__connection_pool.getconn()

    @classmethod
    def return_connection(cls, connection):
        return cls.__connection_pool.putconn(connection)

    @classmethod
    def close_all_connections(cls):
        Database.__connection_pool.closeall()



class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exception_type, exception_val, exception_tb):
        if exception_val is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        Database.return_connection(self.connection)





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