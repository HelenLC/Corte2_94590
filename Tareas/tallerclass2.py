import random

def lista_aleatoria():
    lista = []
    for i in range(10):
        lista.append(random.randint(1, 50))
    return lista
def mayor(lista):
    mayor = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
    print("El número mayor de la lista es:", mayor)

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def primos(lista):
    numeros_primos = []
    for numero in lista:
        if es_primo(numero):
            numeros_primos.append(numero)
    if len(numeros_primos) == 0:
        print("No hay números primos en la lista.")
    else:
        print("Los números primos en la lista son:", numeros_primos)


lista = lista_aleatoria()
print("La lista generada es:", lista)
mayor(lista)
primos(lista)

if __name__=="__main__":
    main()
