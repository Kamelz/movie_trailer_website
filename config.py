import tmdbsimple as tmdb
import sys


class Config():

    """
    'Config'  A configuration class to set our necessary
    configurations far from the application logic.

    """

    def __init__(self):
        """Inits Config class and sets the api key."""
        tmdb.API_KEY = self.get_api_key()  # Assign the API_KEY to the library.

    def get_api_key(self):
        """Return the movie database api key."""
        str = open('config.ini', 'r').read()  # Opens config.ini file.

        if(str[0:8] != "API_KEY=" or str[8:None] == "" ):
            # Check if the api key constant is valid in config.ini.
            error = "Invalid configurations, please make sure that you"
            error = error + "set your api key in config.ini"
            error = error + "file in this format 'API_KEY=XXXXXXX'."
            print(error)
            sys.exit()
            return
        return str[8:None]  # Return the string after API_KEY= .
