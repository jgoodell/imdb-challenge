from movies import (Movie,
                    Genre,
                    Session,
                    )


if __name__ == "__main__":
    movies = list()
    raw_lines = open("movie_metadata.csv", "rb").readlines()

    raw_movie_list = [str(line).split(',') for line in raw_lines]
    movies = Movie.movie_factory(raw_movie_list)
    [movie for movie in movies]
