

import csv


with open ('movie_data.csv', encoding="utf8") as csvfile:
    lista_peliculas = list(csv.DictReader(csvfile))


header = lista_peliculas[0].keys()

print (header)

ganadora = 'Oscar: Mejor película'
lista_ganadoras = []


for pelicula in lista_peliculas:
    try:
        for  columna, valor in pelicula.items(): 
            if columna == 'awards':
                if ganadora in valor:
                    
                    lista_ganadoras.append((pelicula.get('year') + ' - ' + pelicula.get('title')+ ' ' + pelicula.get('average_rating') ))
                    
    except:
        print("error")

print (lista_ganadoras)

#  print("{} - {}".format(pelicula.get('year'), pelicula.get('title')))
