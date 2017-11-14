import webbrowser


class Movie():

    """
    'Movie'  A movie class that helps you to store your favorite movies.

     Attributes:
        movie_title: A string of the movie title.
        movie_storyline: A string of the movie storyline.
        poster_image: A string of the movie image poster url.
        trailer_youtube: A string of the movie trailer url.
        imdb_rate: An integer that indicates the movie rate based on IMDB website.
        genre: An array of movie genre.
        duration: A string of the movie time duration.
        rat: A string of the movie rate ex:R,PG .. etc .
        
    
    """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, imdb_rate, genre, duration, rate):
        """Inits Movie with movie data."""
        self.title = movie_title #Movie title
        self.storyline = movie_storyline #Movie storyline
        self.poster_image_url = poster_image #Movie poster image
        self.trailer_youtube_url = trailer_youtube #Movie trailer
        self.imdb_rate = imdb_rate #Movie IMDB rate
        self.genre = genre #Movie genre
        self.duration = duration #Movie duration
        self.rate = rate #Movie rate

    def show_trailer(self):
        """'show_trailer' Opens a web browser and play the movie youtube trailer that was set using the class instance."""
        webbrowser.open(self.trailer_youtube_url) # Open web browser and runs the targeted url
