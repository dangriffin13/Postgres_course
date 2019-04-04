from movie import Movie
from user import User


first = Movie("The Matrix", "Sci-Fi")
second = Movie("Castaway", "Drama")
third = Movie("Love, Actually", "Rom Com")

user = User("Dan G")

for movie in [first, second, third]:
    user.movies.append(movie)

print(user.movies)

user.send_to_file()

user_from_file = user.load_from_file('Elon M.csv')

print(user_from_file.name)
print(user_from_file.movies)

