import csv
import operator

with open ('movie_data.csv', encoding="utf8") as csvfile:
    lista_peliculas = list(csv.DictReader(csvfile))


def obetener_menu_decadas():
  
    decadas = []
    for pelicula in lista_peliculas:
            
        decadas.append(pelicula.get('year')[0:3] + '0')
        
    
    decadas = list(set(decadas))
    decadas_ordenada =sorted (decadas) 
    

    for i in range(1,len(decadas_ordenada)):
        print ("{} - {}".format(i, decadas_ordenada[i] ))
        
   
def devolver_decada(opcion):
    decadas = []
    for pelicula in lista_peliculas:
            
        decadas.append(pelicula.get('year')[0:3] + '0')
        
    
    decadas = list(set(decadas))
    decadas_ordenada =sorted (decadas) 
    

    for i in range(1,len(decadas_ordenada)):
        if i == opcion:
            return decadas_ordenada[i] 

#print (devolver_decada(2))

def obtener_ranking(decada_elegida,genero_elegido):
    header = lista_peliculas[0].keys()
    lista_ganadoras =[]
    id = 0
    
    genero  = []

    decada_elegida =decada_elegida 
    genero = genero_elegido


    for pelicula in lista_peliculas:
        try:
            for  columna, valor in pelicula.items(): 
                if columna == 'year':
                    if decada_elegida == valor[0:3] + '0':       
                        pelicula_ganadoras = {}
                        if pelicula.get('average_rating')!='' and genero.lower() in pelicula.get('genre').lower():
                            pelicula_ganadoras['year'] = pelicula.get('year') 
                            pelicula_ganadoras['title'] = pelicula.get('title')
                            pelicula_ganadoras['rating'] =  pelicula.get('average_rating')
                            pelicula_ganadoras['genre'] =  pelicula.get('genre')
                            lista_ganadoras.append(pelicula_ganadoras)
                        
        except:
            print("error")

    #print (lista_ganadoras)

    lista_ganadoras_ordenada = sorted(lista_ganadoras, key=lambda k: k['rating'], reverse=True)
    header_ganadoras = ['year','title','rating','genre']
    #print (header_ganadoras)

    with open ('gandoras.csv', 'w', newline='') as csvfile_ganadoras:
        writer = csv.DictWriter(csvfile_ganadoras, fieldnames=header_ganadoras)
        writer.writeheader()
        writer.writerows(lista_ganadoras_ordenada)
    csvfile_ganadoras.close

                        
    r = 0

    if decada_elegida != '':
        print ("\nDecada:", decada_elegida)


    if genero != '':
        print ("Genero:", genero)

    print ("\n{:3} - {:6} {:50}  {}".format("Top", "Año","Titulo","Puntaje"))  

    for pelicula_oscar in lista_ganadoras_ordenada:
        r += 1
        print ("{:3} - {:6} {:50}  {}".format(r, pelicula_oscar['year'],pelicula_oscar['title'],pelicula_oscar['rating']))  

