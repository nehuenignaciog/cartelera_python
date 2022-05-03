
import procesar_movie_data

decada = ''

print ("Bienvenido Cartelera!!")
print ("Su ranking de peliculas premiadas.\n")

print ("Por favor seleccione una decada:")
print ("Deje vacio y presiene Enter si desea ver todas.")
procesar_movie_data.obetener_menu_decadas()
opcion_elegida = int(input())

decada_elegida =  procesar_movie_data.devolver_decada(opcion_elegida)

print ("Escriba un genero:")
genero_elegido = str(input())

procesar_movie_data.obtener_ranking(decada_elegida,genero_elegido)
