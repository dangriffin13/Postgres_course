from user import User

my_user = User('ray@aol.com', 'Ray', 'Smith', None)

my_user.save_to_db()

user_from_db = User.load_from_db_by_email('ray@aol.com')

print(user_from_db)