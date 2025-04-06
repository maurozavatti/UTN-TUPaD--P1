#importo statistics y random para el ejercio 6
from statistics import mode, median, mean
import random

#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

#edad = int(input("Ingrese su edad: "))

#if edad >= 18:
#    print("Es mayor de edad")
#else:
#    print("No es mayor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

#nota = int(input("Ingrese su nota: "))

#if nota >= 6:
#    print("Aprobado")
#else:
#    print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla . Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

#num = int(input("Ingrese un numero: "))

#if num % 2 == 0:
#    print("Ha ingresado un número par")
#else:
#    print("Por favor, ingrese un número par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.

#edad = int(input("Ingrese su edad: "))

#if edad < 12:
#    print("Pertenece a categoria: Niño/a")
#elif edad >= 12 and edad < 18:
#  print("Pertenece a categoria: Adolescente")
#elif edad >= 18 and edad < 30:
#    print("Pertenece a categoria: Adulto/a joven")
#else:
#    print("Pertenece a categoria: Adulto")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

#password = input("Ingrese una contraseña: ")

#if len(password) >= 8 and len(password) <= 14:
#    print("Ha ingresado una contraseña correcta")
#else:
#    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6) El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el siguiente: from statistics import mode, median, mean mi_lista = [1,2,5,5,3] mean(mi_lista) En la documentación oficial se puede encontrar más información sobre este paquete: https://docs.python.org/es/3.8/library/statistics.html. La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio: ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda. ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda. ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
#Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#Definir la lista numeros_aleatorios de la siguiente forma: import random numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
#Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria.

#defino la lista de numeros random con randint (se va a utilizar 50 numero del 1 al 100)
#numeros_aleatorios = [random.randint(1, 100) for i in range (50)]
#defino las variables
#media = mean(numeros_aleatorios)
#mediana = median(numeros_aleatorios)
#moda = mode(numeros_aleatorios)
#imprimo los resultados obtenidos asi se muestran en consola
#print(f'Numeros aleatorios:  {numeros_aleatorios}')
#print(f'Media = {media}')
#print(f'Mediana = {mediana}')
#print(f'Moda = {moda}')
#Operadores Condicioneles
#if media > mediana > moda:
#    print("Sesgo positivo (a la derecha)")
#elif media < mediana < moda:
#    print("Sesgo negativo (a la izquierda)")
#elif media == mediana == moda:
#    print("No hay Sesgo")
#else:
#    print("La distribucion no cumple con las condiciones exactas de sesgo definidas.")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

#palabra = input("Ingrese una palabra o una frase: ")
#pongo condicion si el ultimo caracter de lo ingresado ([-1]) esta dentro de la tupla que contiene las vocales, se le agrega el signo !
#con .lower() para todo lo ingresado a minusculas para trabajar con mayusculas o minisculas en mi condicional
#if palabra[-1].lower() in ("a","e","i","o","u"):
#    print(palabra + "!")
#else:
#    print(palabra)


#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

#nombre = input("Ingrese su nombre: ")
#opcion_nombre = int(input("Ingrese la opcion deseada (1 para mayusculas, 2 para minusculas, 3 para primera letra mayuscula): "))

#if opcion_nombre == 1:
#    print(nombre.upper())
#elif opcion_nombre == 2:
#    print(nombre.lower())
#elif opcion_nombre == 3:
#    print(nombre.title())
#else:
#    print("ERROR!, opcion no valida")

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

#magnitud = float(input("Ingrese la magnitud del terremoto: "))

#if magnitud < 3:
#    print("Muy leve (imperceptible)")
#elif 3 <= magnitud < 4:
#    print("Leve (ligeramente perceptible)")
#elif 4 <= magnitud < 5:
#    print("Moderado (sentido por personas, pero generalmente no causa daños)")
#elif 5 <= magnitud < 6:
#    print("Fuerte (puede causar daños en estructuras debiles)")
#elif 6 <= magnitud < 7:
#    print("Muy Fuerte (puede causar daños significativos)")
#else:
#    print("Extremo (puede causar graves daños a gran escala)")

#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
# Estaciones del año según el hemisferio:
#
# +-----------------------------+----------------------+----------------------+
# |        Periodo del año     | Hemisferio Norte     | Hemisferio Sur       |
# +-----------------------------+----------------------+----------------------+
# | 21 de diciembre - 20 marzo | Invierno             | Verano               |
# | 21 de marzo - 20 junio     | Primavera            | Otoño                |
# | 21 de junio - 20 septiembre| Verano               | Invierno             |
# | 21 de septiembre - 20 dic  | Otoño                | Primavera            |
# +-----------------------------+----------------------+----------------------+
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("Ingrese el Hemisferio donde se encuentra (N/S): " ).upper()
mes = int(input("Ingrese el Mes (1 a 12): " ))
dia = int(input("Ingrese el Dia (1 a 31): " ))

#voy a utilizar funciones para dividir entre Norte y Sur

# Función para determinar estación en el hemisferio norte
def estacion_norte(mes, dia):
    #del 21 de diciembre al 20 de marzo
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        return "Invierno"
    #del 21 de marzo al 20 de junio
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        return "Primavera"
    #del 21 de junio al 20 de septiembre
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        return "Verano"
    #del 21 de septiembre al 20 de diciembre
    elif (mes == 9 and dia >= 21) or (10 <= mes <= 11) or (mes == 12 and dia <= 20):
        return "Otoño"

# Función para determinar estación en el hemisferio sur
# la misma que la anterior pero retornando la estacion contraria
def estacion_sur(mes, dia):
    #del 21 de diciembre al 20 de marzo
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        return "Verano"
    #del 21 de marzo al 20 de junio
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        return "Otoño"
    #del 21 de junio al 20 de septiembre
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        return "Invierno"
    #del 21 de septiembre al 20 de diciembre
    elif (mes == 9 and dia >= 21) or (10 <= mes <= 11) or (mes == 12 and dia <= 20):
        return "Primavera"

# Lógica para mostrar resultado
if hemisferio == "N":
    estacion = estacion_norte(mes, dia)
    print("Estás en el hemisferio norte. La estación es:", estacion)
elif hemisferio == "S":
    estacion = estacion_sur(mes, dia)
    print("Estás en el hemisferio sur. La estación es:", estacion)
else:
    print("Hemisferio no válido. Usá 'N' para norte o 'S' para sur.")





