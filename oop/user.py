from movie import Movie
import csv

class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User Object: {}>".format(self.name)

    def add_movie(self, name, genre):
        movie = Movie(name, genre, False)
        self.movies.append(movie)

    def delete_movie(self, name):
        movies = self.movies

        i = 0
        while movies[i].name != name and i < len(movies):
            i += 1

        if movies[i].name == name:
            del self.movies[i]
        else:
            print('Movie not found')


    def watched_movies(self):
        return [movie for movie in self.movies if movie.watched]

    def send_to_file(self):
        with open("{}.csv".format(self.name), mode='w') as f:
            movie_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            movie_writer.writerow([self.name])
            for movie in self.movies:
                movie_writer.writerow([movie.name, movie.genre, str(movie.watched)])
                #f.write("{},{},{}\n".format(movie.name, movie.genre, str(movie.watched)))


    def load_from_file(self, filename):
        with open(filename,'r') as f:
            csv_reader = csv.reader(f, delimiter=',', quotechar='"')
            username = next(csv_reader)

            movies = []
            for row in csv_reader:
                movie_data = row
                movies.append(Movie(movie_data[0], movie_data[1], movie_data[2] == "True"))

            user = User(username)
            user.movies = movies
            return user