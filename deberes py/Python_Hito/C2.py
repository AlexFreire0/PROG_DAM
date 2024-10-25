from random import *
maquina_victoria = 0
humano_victoria = 0
#creamos una función para cada vez que accedemos al menú principal con las victorias
def menu_principal(humano_victoria, maquina_victoria):
    print("\n1 - Piedra | 2 - Papel | 3-Tijera ")
    numero_humano = int(input("\nElija por favor: "))
    numero_maquina = randint(1, 3)
    decidir(numero_humano, numero_maquina, humano_victoria, maquina_victoria)
#creamos la función en la que se lleva a cabo el resultado junto con las victorias para modificarlas
def decidir(numeroh, numerom, humano_victoria, maquina_victoria):
    match numeroh:
        case 1:
            if numerom == 2:
                print("\nHas perdido!!!  : )")
                maquina_victoria += 1
               
            elif numerom == 3:
                print("\nHas ganado!!!  : )")
                humano_victoria += 1
            else:
                print("\nHabéis empatado")


        case 2:
            if numerom == 3:
                print("\nHas perdido!!!  : )")
                maquina_victoria += 1
               
            elif numerom == 1:
                print("\nHas ganado!!!  : )")
                humano_victoria += 1
            else:
                print("\nHabéis empatado")
        case 3:
            if numerom == 1:
                print("\nHas perdido!!!  : )")
                maquina_victoria += 1
            elif numerom == 2:
                print("\nHas ganado!!!  : )")
                humano_victoria += 1
            else:
                print("\nHabéis empatado")
        case _:
                print("\nPruebe de nuevo, por favor")
                menu_principal()
    if maquina_victoria == 3:
        print("\nHa perdido 3 veces, pruebe suerte la próxima vez.\n")
    else:
        if humano_victoria == 3:
            print("Has ganado!!! Gracias por jugar.\n")
        else:
            menu_principal(humano_victoria, maquina_victoria) #reiniciamos el ciclo hasta ganar o perder 3 veces
menu_principal(humano_victoria, maquina_victoria) #Llamamos a el menú principal