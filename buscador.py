# importing the module
import imdb
from imdb import Cinemagoer

# create an instance of the Cinemagoer class
ic = Cinemagoer()

# creating instance of IMDb
ia = imdb.IMDb()

movie = ia.get_movie('660458')

print (movie)


# movie name

movies = ic.get_keyword('dystopia')
print (len(movies))



name = "3 idiots"

# searching the movie
search = ia.search_movie(name)
 



# printing the result
for i in search:
	print(i)

# print(search)

# get a movie

# print the names of the directors of the movie
print('Directors:')
for director in movie['directors']:
    print(director['name'])

# print the genres of the movie
print('Genres:')
for genre in movie['genres']:
    print(genre)
