from media import Movie
import fresh_tomatoes

movie_title = "Toy Story"
storyline = """ Woody (Tom Hanks), a good-hearted cowboy doll
who belongs to a young boy named Andy (John Morris),
sees his position as Andy's favorite toy jeopardized when
his parents buy him a Buzz Lightyear (Tim Allen) action figure.
Even worse, the arrogant Buzz thinks he's a real spaceman on a
mission to return to his home planet. When Andy's family
moves to a new house, Woody and Buzz must escape the clutches
of maladjusted neighbor Sid Phillips (Erik von Detten)
andreunite with their boy.
"""
poster_url = """https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-
20810-m8zzyx_5670999f.jpeg?region=0%2C0%2C300%2C450"""
trailer_youtube = "https://www.youtube.com/watch?v=KYz2wyBy3kc"
imdb_rate = "8.3"
genre = ["Animation", "Adventure", "Comedy"]
duration = " 1h 21min"
rate = "PG"

toystory = Movie(
    movie_title,
    storyline, poster_url,
    trailer_youtube,
    imdb_rate,
    genre,
    duration,
    rate
)

movie_title = "Reservoir Dogs"
storyline = """A group of thieves assemble to pull of the perfect
diamond heist. It turns into a bloody ambush when one of the men
turns out to be a police informer. As the group begins to question
each other's guilt, the heightening tensions threaten to explode
the situation before the police step in.
"""
poster_url = """http://t3.gstatic.com/images?q=tbn:ANd9GcTPwt7t2o
-jpIcQRIx-6wWtPQqTcrFQmBku_q6QTfPjyN2-5sS-
"""
trailer_youtube = "https://www.youtube.com/watch?v=vayksn4Y93A"
imdb_rate = "8.3"
genre = ["Crime", "Drama", "Thriller"]
duration = " 1h 39min"
rate = "R"

reservoir_dogs = Movie(
    movie_title,
    storyline,
    poster_url,
    trailer_youtube,
    imdb_rate,
    genre,
    duration,
    rate
)

movie_title = "Donnie Darko"
storyline = """In a funny, moving and distinctly mind-bending journey
through suburban America, one extraordinary but disenchanted teenager
is about to take Time's Arrow for a ride. After surviving a freak accident,
Donnie (Jake Gyllenhaal) begins to explore what it means to be alive,
and in short order to be in love, he uncovers secrets of the universe that
give him a tempting power to alter time and destiny
"""
poster_url = """https://upload.wikimedia.org/wikip
edia/en/d/db/Donnie_Darko_poster.jpg
"""
trailer_youtube = "https://www.youtube.com/watch?v=ZZyBaFYFySk"
imdb_rate = "8.1"
genre = ["Sci-Fi", "Drama", "Thriller"]
duration = " 1h 53min "
rate = "R"

donnie_darko = Movie(
    movie_title,
    storyline,
    poster_url,
    trailer_youtube,
    imdb_rate,
    genre,
    duration,
    rate
)

movie_title = "Pulp Fiction"
storyline = """Vincent Vega (John Travolta) and Jules Winnfield
(Samuel L. Jackson) are hitmen with a penchant for philosophical
discussions. In this ultra-hip, multi-strand crime movie, their
storyline is interwoven with those of their boss, gangster
Marsellus Wallace (Ving Rhames) ; his actress wife,
Mia (Uma Thurman) ; struggling boxer Butch Coolidge
(Bruce Willis) ; master fixer Winston Wolfe
(Harvey Keitel) and a nervous pair of armed robbers
"""
poster_url = """http://www.gstatic.com/tv/
thumb/movieposters/15684/p15684_p_v8_ac.jpg
"""
trailer_youtube = "https://www.youtube.com/watch?v=s7EdQ4FqbhY"
imdb_rate = "8.9"
genre = ["Crime", "Drama"]
duration = " 2h 34min"
rate = "R"

pulp_fiction = Movie(
    movie_title,
    storyline,
    poster_url,
    trailer_youtube,
    imdb_rate,
    genre,
    duration,
    rate
)

movie_title = "Wreck-It Ralph"
storyline = """Arcade-game character Wreck-It Ralph (John C. Reilly) is tired
of always being the bad guy and losing to his good guy opponent, Fix-It Felix
(Jack McBrayer). Finally, after decades of seeing all the glory go to Felix,
Ralph decides to take matters into his own hands. He sets off on a game-hopping
trip to prove that he has what it takes to
be a hero. However, while on his quest, Ralph accidentally
unleashes a deadly enemy that threatens the entire arcade.
"""
poster_url = """http://t3.gstatic.com/images?q=tbn:ANd9GcR6e2NEBAIaJQ8_-1KSrUc1NKu
yBWAK0ch7DerecaEhYEow1dnL
"""
trailer_youtube = "https://www.youtube.com/watch?v=87E6N7ToCxs"
imdb_rate = "7.7"
genre = ["Animation", "Adventure", "Comedy"]
duration = " 1h 41min"
rate = "PG"

wreck_it_ralph = Movie(
    movie_title,
    storyline,
    poster_url,
    trailer_youtube,
    imdb_rate,
    genre,
    duration,
    rate
)

movie_title = "Finding Nemo"
storyline = """Marlin (Albert Brooks), a clown fish, is overly cautious with
his son, Nemo (Alexander Gould), who has a foreshortened fin.
When Nemo swims too close to the surface to prove himself,
he is caught by a diver, and horrified Marlin must set out
to find him. A blue reef fish named Dory (Ellen DeGeneres)
-- who has a really short memory -- joins Marlin and complicates
the encounters with sharks, jellyfish, and a host of ocean dangers.
Meanwhile, Nemo plots his escape from a dentist's fish tank.
"""

poster_url = """http://t1.gstatic.com/images?q=tbn:ANd9GcSoStMb2jeN136xQhf
2g3ROpTB9Dker9IlfGbMbwYB3ruC9VcOj
"""
trailer_youtube = "https://www.youtube.com/watch?v=SPHfeNgogVs"
imdb_rate = "8.1"
genre = ["Animation", "Adventure", "Comedy"]
duration = " 1h 40min"
rate = "R"

finding_nemo = Movie(
    movie_title,
    storyline,
    poster_url,
    trailer_youtube,
    imdb_rate,
    genre, duration,
    rate
)

movies = [
    toystory,
    reservoir_dogs,
    donnie_darko,
    pulp_fiction,
    wreck_it_ralph,
    finding_nemo
]

# -------------------------Main App---------------------------------

# generates a static website with your favorites movies.
fresh_tomatoes.open_movies_page(movies)
