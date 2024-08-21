import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import array

# Crear un array de enteros (Paréntesis).
mi_array = array.array('i', [1, 2, 3, 4, 5])
print(mi_array)
#Este es un array de strings
alumnos = ("nacho", "juan", "pedro", "luis")


# Crear una lista (Corchetes).
mi_lista = [1, 2, 3, 4, 5]
print(mi_lista)

# Crear un diccionario
mi_diccionario = {
    'nombre': 'Nacho',         # Similar a un Json, donde cada elemento tiene una clave y un valor.
    'edad': 25,
    'ciudad': 'Buenos Aires'
}
print(mi_diccionario)


#GOOGLE COLAB

##Para leer archivos: 
#from google.colab import drive #De la librería de google.colab importamos la función drive.
#drive.mount('/content/drive') #Mount es una función que nos conecta el drive con el colab.

## Ejemplo de acceso a un archivo en Google Drive.
#ruta_archivo = '/content/drive/My Drive/mi_carpeta/mi_archivo.txt'

##Cargar el archivo en un dataframe
#df = pd.read_excel(ruta_archivo) #la función read_excel viene de la librería pandas. Convierte el excel en un dataframe.

##Imprimir las primeras 5 filas del dataframe.
#print(df.head()) #La función head() nos muestra por default las primeras 5 filas del dataframe. Si quisieramos ver las primeras 10, tendríamos que poner head(10).

##Copiar el dataframe para no modificar el original.
#df_modified = df.copy()

##Función que actualiza el promedio de juguetes comprados en función de los ingresos.
#def actualizar_promedio_juguetes(row): #Definimos una función que toma como parámetro una fila del dataframe.
#    if row['Ingresos'] > 20000:
#        row['Promedio_Juguetes_Comprados'] = 3 #Si el ingreso es mayor a 20000, el promedio de juguetes comprados es 3.
#    return row #Nos devuelve 3 si el ingreso es mayor a 20000.

##Aplicar la función a cada fila del dataframe
#df_modified = df_modified.apply(actualizar_promedio_juguetes, axis=1) #La función apply() aplica una función a cada fila del dataframe. Axis=1 indica que la función se aplica a cada fila. Si fuese axis=0, la función se aplicaría a cada columna.



#Solicitar al usuario que ingrese una palabra.
palabra = input("Ingrese una palabra: ")
print("La palabra que ingresaste es: " + palabra)

#Usar un bucle FOR para imprimir cada letra de la palabra.
for letra in palabra:
    print(letra)

#Creo una lista con nombres y edades.
personas= ["Nacho", 22, "Juan", 23, "Pedro", 24]

#Imprimir solo los nombres de las personas.
for elemento in personas:
    if isinstance(elemento, str):
        print(elemento)


#ACTIVIDADES LESSON 4 AI PYTHON FOR BEGINNERS

# Write code that displays your favorite color
color = input("Ingrese su color favorito: ")
print("Tu color favorito es: " + color)

# Write code that answers the question "How are you feeling today?"
humor = input("¿Cómo te sientes hoy? ")
print("Te sientes: " + humor)

# Alter your code from the previous cell so that it will cause an error when you run it
#print(bien)

# Ask an LLM to help you fix the error in the code in the previous cell (or fix yourself) and then type the corrected code on the next line:
bien = "Todo está bien"
print(bien)



