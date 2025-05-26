import math
from collections import deque

#1) Dado el diccionario precios_frutas precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450} Añadir las siguientes frutas con sus respectivos precios:
# ●​ Naranja = 1200
# ●​ Manzana = 150

#precios_frutas = {'Banana': 1200,
#                'Ananá': 2500, 
#                'Melón': 3000, 
#                'Uva':1450}

#precios_frutas['Naranja'] = 1200
#precios_frutas['Manzana'] = 150
#print(precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#●​ Banana = 1330
#●​ Manzana = 1700
#●​ Melón = 2800

#precios_frutas['Banana'] = 1330
#precios_frutas['Manzana'] = 1700
#precios_frutas['Melon'] = 2800

#print(precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios

#lista_frutas = []
#for i in precios_frutas:
#    lista_frutas.append(i)

#otra forma de hacerlo es con la propiedad .keys()
#lista_frutas = list(precios_frutas.keys())

#print(lista_frutas)

#4) Crear una clase llamada Persona que contenga un método __init__ con los atributos nombre, pais y edad y el método saludar. El método saludar debe imprimir por pantalla un mensaje de salud que siga la estructura "¡Hola! Soy [nombre], vivo en [pais] y tengo [edad] años."

#class Persona:
#    def __init__(self, nombre, pais, edad):
#        self.nombre = nombre
#        self.pais = pais
#        self.edad = edad
        
#    def saludar(self):
#        print(f"Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")

#nombre = input("Ingrese su nombre: ")
#edad = int(input("Ingrese su edad: "))
#pais = input("Ingrese su pais de residencia: ")  

#persona1 = Persona(nombre, pais, edad)

#persona1.saludar()

#5) Crear una clase llamada Circulo que contenga el atributo radio y los métodos calcular_area y calcular_perimetro. Dichos métodos deben calcular el parámetro correspondiente.
# Ayuda: el módulo math puede ser de utilidad para usar la constante 𝜋.

#class Circulo:
#    def __init__(self, radio):
#        self.radio = radio
        
#    def calcular_area(self):
#        return math.pi * (self.radio ** 2)
    
#    def calcular_perimetro(self):
#        return 2 * math.pi * self.radio 
    
#radio = float(input("Ingrese el radio: "))

# Creamos una instancia de la clase Circulo
#circulo = Circulo(radio)

# Llamamos a los métodos para calcular el área y el perímetro
#area = circulo.calcular_area()
#perimetro = circulo.calcular_perimetro()

#print(f"El area es {area:.2f}")
#print(f"El perimetro es {perimetro:.2f}")


#6) Dado un string con paréntesis "()", "{}", "[]", verifica si están correctamente balanceados usando una pila.Ejemplo de entrada y salida:
    #balanceado("({[]})") -> True
    #balanceado("({[})") -> False
    
#def balanceado(cadena):
#    pila = []  # Creamos una pila vacía
    # Diccionario que mapea los paréntesis de apertura con los de cierre correspondientes
#    pares = {')': '(', '}': '{', ']': '['}
    
#    for i in cadena:
#        if i in pares.values():  # Si es un paréntesis de apertura
#            pila.append(i)
#        elif i in pares.keys():  # Si es un paréntesis de cierre
#            if pila and pila[-1] == pares[i]:  # Comprobamos si el último paréntesis es el correspondiente
#                pila.pop()  # Si es válido, lo eliminamos de la pila
#            else:
#                return False  # Si no es válido, retornamos False
    
    # Si la pila está vacía, significa que todo está balanceado
#    return len(pila) == 0

# Ejemplos de uso
#print(balanceado("({[]})"))  # True
#print(balanceado("({[})"))   # False

#7) Usa una cola para simular un sistema de turnos en un banco. La cola debe permitir:
#●​ Agregar clientes (encolar).
#●​ Atender clientes (desencolar).
#●​ Mostrar el siguiente cliente en la fila.

#class Cola:
#    def __init__(self):
#        self.elementos = deque()

#agregamos un elemento a la cola
#    def encolar(self,elemento):
#        self.elementos.append(elemento)

#quitamos un elemento a la cola, pero verificamos sino esta vacia
#    def desencolar(self):
#        return self.elementos.popleft() if not self.esta_vacia() else "La cola esta vacia"
    
#para vefificar si la cola esta vacia
#    def esta_vacia(self):
#        return len(self.elementos) == 0

#mostramos el que esta, o queda al frente de la cola (el siguiente cliente en la fila)
#    def ver_frente(self):
#        return self.elementos[0] if not self.esta_vacia() else "La cola esta vacia"

##Ejemplo de cola de banco

#cola_banco = Cola() #le declaro una variable a la clase Cola

#encolo los clientes llamando al metodo encolar
#cola_banco.encolar("Cliente 1")
#cola_banco.encolar("Cliente 2")
#cola_banco.encolar("Cliente 3")

#imprimo los clientes desoncolados y los quedan al frente
#print(cola_banco.ver_frente()) #Cliente 1
#print(cola_banco.desencolar()) #Cliente 1
#print(cola_banco.ver_frente()) #Cliente 2
#print(cola_banco.desencolar()) #Cliente 2
#print(cola_banco.ver_frente()) #Cliente 3
#print(cola_banco.desencolar()) #Cliente 3
#print(cola_banco.ver_frente()) #La cola esta vacia


#8) Crea una lista enlazada que permita insertar nodos al inicio y recorrer la lista para mostrar los valores almacenados.

# Definimos un nodo
#class Nodo:
#    def __init__(self, valor):
#        self.valor = valor
#        self.siguiente = None

# Definimos la lista enlazada
#class ListaEnlazada:
#    def __init__(self):
#        self.cabeza = None  # inicio de la lista

#    # Insertar al inicio
#    def insertar_al_inicio(self, valor):
#        nuevo_nodo = Nodo(valor)
#        nuevo_nodo.siguiente = self.cabeza
#        self.cabeza = nuevo_nodo

#    # Recorrer y mostrar valores
#    def mostrar(self):
#        actual = self.cabeza
#        while actual:
#            print(actual.valor)
#            actual = actual.siguiente

#lista = ListaEnlazada()
#lista.insertar_al_inicio(10)
#lista.insertar_al_inicio(20)
#lista.insertar_al_inicio(30)

#lista.mostrar()

#9) Dada una lista enlazada, implementa una función para invertirla.

#class Nodo:
#    def __init__(self, valor):
#        self.valor = valor
#        self.siguiente = None

#class ListaEnlazada:
#    def __init__(self):
#        self.cabeza = None

#    def insertar_al_inicio(self, valor):
#        nuevo_nodo = Nodo(valor)
#        nuevo_nodo.siguiente = self.cabeza
#        self.cabeza = nuevo_nodo

#    def mostrar(self):
#        actual = self.cabeza
#        while actual:
#            print(actual.valor, end=" -> ")
#            actual = actual.siguiente
#        print("None")

#    def invertir(self):
#        anterior = None
#        actual = self.cabeza
#        while actual:
#            siguiente = actual.siguiente
#            actual.siguiente = anterior
#            anterior = actual
#            actual = siguiente
#        self.cabeza = anterior

#lista = ListaEnlazada()
#lista.insertar_al_inicio(1)
#lista.insertar_al_inicio(2)
#lista.insertar_al_inicio(3)

#print("Original:")
#lista.mostrar()  # 3 -> 2 -> 1 -> None

#lista.invertir()

#print("Invertida:")
#lista.mostrar()  # 1 -> 2 -> 3 -> None