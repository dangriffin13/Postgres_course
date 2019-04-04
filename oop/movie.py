
class Movie:
    def __init__(self, name, genre, watched=False):
        self.name = name
        self.genre = genre
        self.watched = watched

    def __repr__(self):
        return "<Movie Object: {}>".format(self.name)
        


if __name__ == "__main__":
   print("Movie class launched")