import media
import fresh_tomatoes
import config

# Configure the movie API.
config.Config()

# Toy Story instance of Movie class
toystory = media.Movie(862)


# Reservoir Dogs instance of Movie class
reservoir_dogs = media.Movie(500)


# Donnie Darko instance of Movie class
donnie_darko = media.Movie(141)


# Pulp Fiction instance of Movie class
pulp_fiction = media.Movie(680)


# Wreck-It Ralph instance of Movie class
wreck_it_ralph = media.Movie(82690)

# Finding Nemo instance of Movie class
finding_nemo = media.Movie(12)


# movies array that sotres the instance of Movie class.
movies = [toystory, reservoir_dogs, donnie_darko,
          pulp_fiction, wreck_it_ralph, finding_nemo]

# generates a static website with your favorites movies.
fresh_tomatoes.open_movies_page(movies)
