def calcular_doble(numero):
    return numero * 2

# Lista de ejemplo
numeros = [1, 2, 3, 4, 5]

# Uso de la función map para aplicar 'calcular_doble' a cada elemento de la lista
dobles = list(map(calcular_doble, numeros))

print(dobles)

    