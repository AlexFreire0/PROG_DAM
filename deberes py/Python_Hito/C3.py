ingresos = 0
ingresos_totales = 0
sacado_total = 0
#Creamos una funcion en la que se ingrese al principio el saldo de la cuenta
def principio(ingresos_totales, sacado_total):
    while True:
        saldo = float(input("Ingrese por favor el saldo actual: ")) #Los floats para lo relacionado a el saldo
        if saldo > 0:
            break
        else:
            print("Porfavor itroduzca un numero positivo.")
    ingresos_totales = ingresos_totales + saldo
    menu(saldo, ingresos_totales, sacado_total)
#Hacemos otra funcion para el menu en el que se indiquen las diferentes operaciones.
def menu(saldo, ingresos_totales, sacado_total):    
    print(f"\nSaldo actual: {saldo} €\n\nQue operación desea hacer?:\n\n 1 - Meter dinero\n 2 - Sacar dinero\n 3 - Estadisticas\n 4 - Salir")
    while True:
        opcion = int(input("Ingrese su operación, por favor: ")) #Integral para las opciones
        match opcion:
            case 1:
                ingresar(saldo, ingresos_totales, sacado_total)
                break
            case 2:
                extraer(saldo, ingresos_totales, sacado_total)
                break
            case 3:
                stats(saldo, ingresos_totales, sacado_total)
                break
            case 4: #case para terminar o dejar salir al usuario de la "aplicación"
                break
            case _:
                print("Opción no valida.")
# Esta funcioin la llamamos cada vez que deseamos hacer un ingreso a la cuenta.
def ingresar(saldo, ingresos_totales, sacado_total):
    while True:
        ingreso = float(input("Introduzca el valor a ingresar: ")) #Los floats para lo relacionado a el saldo
        if ingreso > 0:
            break
        else:
            print("Por favor introduzca un numero positivo.")
    saldo += ingreso
    ingresos_totales += ingreso
    menu(saldo, ingresos_totales, sacado_total)
# Esta funcioin la llamamos cada vez que deseamos sacar dinero de la cuenta.
def extraer(saldo, ingresos_totales, sacado_total):
    while True:
        extraccion = float(input("Introduzca el valor a extraer: ")) #Los floats para lo relacionado a el saldo
        if extraccion > 0:
            break
        else:
            print("Por favor itroduzca un numero positivo.")
    saldo -= extraccion
    sacado_total += extraccion
    menu(saldo, ingresos_totales, sacado_total)
# Esta funcioin la llamamos cada vez que deseamos ver las estadisticas de la cuenta.
def stats(saldo, ingresos_totales, sacado_total):
    print(f"Estadisticas:\n\n - Saldo actual: {saldo} \n - Ingresos totales: {ingresos_totales}\n - Dinero total sacado: {sacado_total}\n")
    input("") #Ponemos un imput para que la persona pueda parar a leer la informacion y que al dar enter siga el recorrido
    
    menu(saldo, ingresos_totales, sacado_total)

principio(ingresos_totales, sacado_total)
    