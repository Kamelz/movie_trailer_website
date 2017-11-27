import webbrowser
import tmdbsimple as tmdb


class Movie():

    """
    'Movie'  A movie class that helps you to store your favorite movies.

    Attributes:
        movie_title: A string of the movie title.
        movie_storyline: A string of the movie storyline.
        poster_image: A string of the movie image poster url.
        trailer_youtube: A string of the movie trailer url.
        imdb_rate: An integer that indicates movie rate based on IMDB website.
        genre: An array of movie genre.
        duration: A string of the movie time duration.
        rat: A string of the movie rate ex:R,PG .. etc .
    """

    def __init__(self, movie_id):
        """Inits Movie with movie id.
        Attributes:
            movie_id: An integer of the movie.
        """
        self.movie_id = movie_id  # Movie id
        self.movie = self.movie_instance()
        self.info()  # request movie information.

    def trailer(self):
        """'trailer' returns the movie trailer."""
        response = self.movie.videos()
        return "https://www.youtube.com/watch?v="+response['results'][0]['key']

    def movie_instance(self):
        """'movie_instance' returns an instance of the Movies
        class with the assigned movie."""
        return tmdb.Movies(self.movie_id)

    def info(self):
        """'info' request the movie info.
        Note: it must be called before you request
        any of the movies basic information"""
        return self.movie.info()

    def get_image_base_url(self):
        """'get_image_base_url' returns the images base url."""
        return "https://image.tmdb.org/t/p/w640"

    def poster(self):
        """'poster' returns the movie poster image url."""
        return self.get_image_base_url() + self.movie.poster_path

    def title(self):
        """'title' returns the movie title."""
        return self.movie.title

    def vote_average(self):
        """'certification' returns the movie average vote."""
        return self.movie.vote_average

    def genres(self):
        """'certification' returns an array of the movie genres."""
        movie_generes = []
        for genere in self.movie.genres:
            movie_generes.append(genere['name'])
        return movie_generes
