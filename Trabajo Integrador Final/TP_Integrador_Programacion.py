import time

lista = [1, 5, 57, 20, 34 , 2, 8, 11, 45, 16, 30]

x = 22

arr= sorted(lista)

print ("Lista ordenada", arr)
print("Buscaremos el numero", x)

def busqueda_interpolacion(arr, x): 
    i = 0   #Indice inicial
    j = len(arr) - 1  #indice final
    pos = 0 #posicion estimada del elemento
    pasos = 0 # hacemos un contador para los pasos realizados
    #Bucle principal
    #controlamos que el indice bajo no sea mayor que el indice alto y 
    # que el valor buscado este dentro del rango actual que es arr[i] a arr[j]
    while i <= j and arr[i] <= x <= arr[j]:
        #Calculamos la posicion estimada (pos) donde podria estar x.
        #evitamos division por cero si los extremos son iguales
        if arr[i] == arr[j]:
            if arr[i] == x:
                return i
            else:
                return -1
        
        #Estimamos la posicion probable de x usando interpolacion lineal.
        #La formula calcula en que punto del interbalo (i a j) podria estar x,
        #suponiendo que los datos estan distribuidos uniformemente.
        #Esto ayuda a reducir la cantidad de pasos en comparacion a una busqueda binaria.

        pos = i + (((x - arr[i]) * (j - i) // (arr[j] - arr[i])))  
        pasos += 1

        if arr[pos] == x:
            print(f"Pasos realizados: {pasos}")
            return pos
        elif arr[pos] < x:
            i = pos + 1
        else:
            j = pos - 1
    
    return -1 #Si no se encuentra

#Usamos time para medir cuanto tarda en ejecutarse la busqueda
inicio = time.time()
busqueda = busqueda_interpolacion(arr, x)
fin = time.time()

if busqueda != -1:
    print(f'El numero {x} esta en la posicion {busqueda}')
else:
    print(f'No se encontro el numero {x}')

print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")