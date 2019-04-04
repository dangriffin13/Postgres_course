from user import User

my_user = User('rolf@rsmith.com', 'Rolf', 'Smith', None)

my_user.save_to_db()


user_from_db = User.load_from_db_by_email('rolf@rsmith.com')

print(user_from_db)