import random
from statistics import mean


#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

#for i in range(1, 101):
#    print(i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

#num = int(input("Ingrese un numero: "))
#caracteres = 0
#for i in str(num):
#    caracteres += 1

#print(f"{num} tiene {caracteres} caracter/es")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

#num1 = int(input("Ingrese el inicio del rango: ")) 
#num2 = int(input("Ingrese el final del rango: "))
#suma = 0

#for i in range(num1 + 1, num2):
#    print(i)
#    suma += i

#print(f"La sumatoria de los numeros comprendidos entre {num1} y {num2} es: {suma}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

#num = int(input("Ingrese un numero (0 para terminar): "))
#suma = 0

#while num !=0:
#    suma += num
#    num = int(input("Ingrese un numero (0 para terminar): "))
#aca tambien si considera los numeros negativos,  si el usuario ingresa un numero negativo, se suma, pero al ser negativo obvio se resta

#armo el bucle para considerar solo los numeros positivos
#while num > 0:
#    suma += num
#    num = int(input("Ingrese un numero (0 para terminar): "))

#print(f"La suma de los numeros ingresados es {suma}")

#la consigna no aclara si los numeros enteros ingresados por el usuario deben ser solo positivos 

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

#num_random = random.randint(0, 10)
#intentos = 1 #inicializa en 1, ya que minimo siempre va a haber un intento 
#num_usuario = int(input("Adivine el numero entre 0 y 9: "))

#mientras el numero ingresado sea diferente al numero random se va a sumar 1 a la varible intentos
#while num_usuario != num_random:
#    intentos += 1
#    num_usuario = int(input("Adivine el numero entre 0 y 9: "))

#print(f"El numero random es {num_random} y fue adivinado en {intentos} intentos")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

#for i in range(100, -1, -2):
#    print(i)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

#num_usuario = int(input("Ingrese un numero: "))
#suma = 0

#while num_usuario <= 0:
#    print("Por favor ingrese un número positivo.")
#    num_usuario = int(input("Ingrese un número positivo: "))

#for i in range(0, num_usuario + 1):
#    suma += i

#print(f"La suma de los numeros comprendidos entre 0 y {num_usuario} es: {suma}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).


#pares= 0
#impares = 0
#negativos = 0
#positivos = 0

#for i in range(100):
#    numeros = int(input(f"Ingrese el número {i+1}°: "))
    
#    if numeros % 2 == 0:
#        pares += 1
#    else:
#        impares += 1
        
#    if numeros > 0:
#        positivos += 1
#    else:
#        negativos +=1 
        
#print(f"La cantidad de numeros pares ingresados es: {pares}")
#print(f"La cantidad de numeros impares ingresados es: {impares}")
#print(f"La cantidad de numeros posistivos ingresados es: {positivos}")
#print(f"La cantidad de numeros negativos ingresados es: {negativos}")


#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

#numeros = []

#for i in range(100):
#    numero = int(input(f"Ingrese el número {i+1}°: "))
#    numeros.append(numero)
    
#media = mean(numeros)

#print(f"La media de los numeros ingresados es: {media}")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

#num = int(input("Ingrese un numero e invertire sus digitos: "))
#num_invertido = 0

#for digito in str(num)[::-1]:
#    num_invertido = num_invertido * 10 + int(digito)
    
#print(f"El numero invertido queda: {num_invertido}")