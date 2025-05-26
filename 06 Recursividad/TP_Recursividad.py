#TP Recursividad
"""1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario"""

def factorial(num):
    if num == 0 or num ==1:
        return 1
    else:
        return num * factorial(num-1)
    
if __name__== "__main__":
    print(factorial(4))
    
"""2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique."""

def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)
    
if __name__== "__main__":
    print(fibonacci(4))
    #en el ejemplo de 4. el resultado es 3, dado a que las dos primeras pos no se tienen en cuenta (0 y 1)
    #El cálculo recursivo para fibonacci(4) es:
        #fibonacci(4) = fibonacci(3) + fibonacci(2)
        #fibonacci(3) = fibonacci(2) + fibonacci(1) = 1 + 1 = 2
        #fibonacci(2) = fibonacci(1) + fibonacci(0) = 1 + 0 = 1
        #Por lo tanto, fibonacci(4) = 2 + 1 = 3

"""3) Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula "𝑛 ^ 𝑚 = 𝑛 ∗ 𝑛 ^ (𝑚−1)". Prueba esta función en un
algoritmo general."""

def potencia(num, exp):
    if exp == 0:
        return 1
    else:
        # Calculo el resultado de la llamada recursiva
        resultado_parcial = num * potencia(num, exp - 1)
        # Imprimo el paso actual
        print(f"{num} * {num}^{exp-1} = {resultado_parcial}")
        return resultado_parcial
        
if __name__== "__main__":
    print(potencia(4,5))

"""4) Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto"""

def convertir_a_binario(num):
    if num == 1:
        return "1"
    elif num == 0:
        return "0"
    else:
        division = num // 2
        resto = num % 2
        print(f"{num} / 2 = {division}(resto = {resto})")
        print(f"{division} % 2 = {resto}")
        return convertir_a_binario(division) + str(resto)
        
if __name__== "__main__":
    print(convertir_a_binario(10))

"""5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.
Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed()."""

def es_palindromo(palabra):
    # Caso base: cadena vacía o de un solo carácter es palíndromo
    if len(palabra) <= 1:
        return True
    # Caso recursivo: comparar primer y último carácter
    if palabra[0].lower() != palabra[-1].lower():
        return False
    # Llamada recursiva con la subcadena sin los extremos
    return es_palindromo(palabra[1:-1])

if __name__== "__main__":
    print(es_palindromo("radar"))
    
"""6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
Ejemplos:
suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
suma_digitos(9) → 9
suma_digitos(305) → 8 (3 + 0 + 5)
"""

def suma_digitos(n):
    if n < 0:
        return f"El numero tiene que ser postivo"
    elif n == 0:
        return 0
    else:
        #Cuando usamos n % 10, obtenemos el último dígito del número ( n ) en base decimal
        digito = n % 10
        resto = n // 10
        print(f"Dígito: {digito}, Resto del número: {resto}")
        return digito + suma_digitos(resto)

if __name__== "__main__":
    print(suma_digitos(2121))
    
"""7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.
Ejemplos:
contar_bloques(1) → 1
(1)
contar_bloques(2) → 3
(2 + 1)
contar_bloques(4) → 10
(4 + 3 + 2 + 1)"""

def contar_digito(numero, digito):
    # Caso base: si el número es 0, no hay más dígitos que contar
    if numero == 0:
        return 0
    # Obtener el último dígito
    ultimo_digito = numero % 10
    # Contar si el último dígito coincide con el dígito buscado (1 si coincide, 0 si no)
    contador = 1 if ultimo_digito == digito else 0
    # Llamada recursiva con el número sin el último dígito
    return contador + contar_digito(numero // 10, digito)
    #Dividimos numero entre 10 (numero // 10) para eliminar el último dígito y llamamos recursivamente a la función.

if __name__=="__main__":
    print(contar_digito(123123123123, 3))
