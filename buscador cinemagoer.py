# importing the module
import imdb
from imdb import Cinemagoer

# create an instance of the Cinemagoer class
ic = Cinemagoer()

# creating instance of IMDb

# movie name

movies = ic.get_keyword('batman')
print (len(movies))

print (movies[0].data)