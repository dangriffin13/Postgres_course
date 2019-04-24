from user import User
from database import Database

Database.initialize(database='learning',
                    user='danielgriffin',
                    password='',
                    host='localhost')

my_user = User('jan@aol.com', 'Janet', 'Smith', None)

#my_user.save_to_db()

user_from_db = User.load_from_db_by_email('rolf@rsmith.com')

print(user_from_db)