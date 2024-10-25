#               -------- Operaciones aritméticas -----------

##Suma (+)
#a = 5 
#b = 3
#resultado = a + b 
#print(resultado) # Mostramos el valor de la suma de a(5) y b(3)
#
##Resta (-)
#a = 10
#b = 4
#resultado = a - b
#print(resultado) # Mostramos el valor de la resta de a(10) y b(4)
#
##Multiplicación (*)
#a = 6
#b = 7
#resultado = a * b
#print(resultado) # Mostramos el valor de la multiplicación de a(6) y b(7)
#
##División (/)
#a = 8
#b = 2
#resultado = a / b
#print(resultado) # Mostramos el valor de la división de a(8) y b(2)
#
##División entera (//)
#a = 9
#b = 4
#resultado = a // b
#print(resultado) # Mostramos el valor de la división de a(9) y b(4) pero sin decimales
#
##Módulo (%)
#a = 10
#b = 3
#resultado = a % b
#print(resultado) # Mostramos el valor de la resta de la división de a(10) y b(3)
#
##Potencia (**)
#a = 2
#b = 3
#resultado = a ** b
#print(resultado) #Mostramos el valor del resultado de elevar a(2) a b(3)
#
##     -------   CADENAS DE TEXTO   ----------
#
## Permitir concadenar (+) 
#nombre = "Juan"
#apellido = "Pérez"
#nombre_completo = nombre + " " + apellido
#print(nombre_completo)
#
##Repetir textos(*)
#frase = "Me voy a caer "
#repetida = frase * 3 # al poner * 3 le especificamos al codigo que debemos repetir 3 veces el string
#print(repetida) # Lo mostramos por pantalla
#
##Acceder a un carácter de una cadena []
#frase = "Python"
#letra = frase[0] #aqui entre corchetes especificamos a que caracter queremos acceder
#print(letra)
#
##Longitud de una cadena (len)
#frase = "Python"
#longitud = len(frase)
#print(longitud) # Nos especifica la cantidad de letras que tiene el string
#
##    ------------   Operaciones con listas -----------
#
## Crear una lista
#mi_lista = [1, 2, 3, 4, 5]
#print(mi_lista)
#
## Acceder a elementos de una lista
#mi_lista = ["manzana", "banana", "cereza"]
#print(mi_lista[1]) #lee el lugar corresondiente de la lista empezando por 0 
#
## Añadir elementos a una lista (append)
#mi_lista = ["manzana", "banana"]
#    # Añade cereza a la lista
#print(mi_lista)
#
## Eliminar elementos de una lista (remove)
#mi_lista = ["manzana", "banana", "cereza"]
#mi_lista.remove("banana") # Elimina banana de la lista
#print(mi_lista)
#
#
# --------------------------------------------------------------------------------------------------------------------------------------------------
#                                           Estructuras condicionales
#------------------------------------------------------------------------------------------------------------------------------------------------------


# --------------------- Valor de entrada dependiendo de la edad -----------------------------
#Precio = 0
#edad = int(input("Escriba su edad por favor: "))
#
#if edad < 5:
#    Precio = 0
#elif edad < 13:
#    Precio = 5
#elif edad < 18:
#    Precio = 7
#else:
#    Precio = 10
#    
#print("El valor de su entrada es:", Precio)
#
##   ----------------------Notas----------------------  No se puede con match case asi tendremos que utilizar el if

#Nota = 0
#
#if Nota >= 90:
#    Calificacion = "A"
#elif Nota >= 80:
#    Calificacion = "B"
#elif Nota >= 70:
#    Calificacion = "C"
#elif Nota >= 60:
#    Calificacion = "B"
#else:
#    Calificacion = "F"
#print("La nota actual tuya es:", Calificacion)
#
#

# ---------------------------- DIAS DE LA SEMANA -------------------------------
#Dia_semana = int(input("Que dia de la semana es del 1-7: "))
#
#match Dia_semana:
#    case 1:
#        print("Lunes") 
#    case 2:
#        print("Martes") 
#    case 3:
#        print("Miercoles") 
#    case 4:
#        print("Jueves") 
#    case 5:
#        print("Viernes") 
#    case 6:
#        print("Sabado") 
#    case 7:
#        print("Domingo") 
#    case _:
#        print("El numero no es valido")

# ----------------------------- Clasificación de usuarios según edad y preferencia de idioma -----------------------
#edad = int(input("Ingrese su edad, porfavor: "))
#
#idioma = input("Porfavor introduzca su idioma. Ej: es   : ")
#
#if edad < 12:
#    print("Usted es un niño")
#elif edad < 18:
#    print("Usted es un adolescente")
#elif edad < 60:
#    print("Usted es un Adulto")
#else:
#    print("Usted es un Adulto mayor")
#    
#match idioma:
#    case "es":
#        print("Has seleccionado el idioma español.")
#    case "en":
#        print("Your selected language is English.")
#    case "fr":
#        print("Votre langue sélectionnée est le français.")
#    case _:
#        print("Idioma no soportado")
#        
#        
        # ----------------------------- Clasificación de vehículos y selección de color preferido --------------------------
#vehiculo = (input("Ingrese su vehículo, porfavor: "))
#
#color = input("Porfavor introduzca el color del vehículo. Ej: azul   : ")
#
#if vehiculo == "coche":
#    print("Vehículo de cuatro ruedas")
#elif vehiculo == "moto":
#    print("Vehículo de dos ruedas")
#elif vehiculo == "bicicleta":
#    print("Vehículo no autorizado")
#else:
#    print("Tipo de vehículo no reconocido")
#    
#match color:
#    case "rojo":
#        print("Has seleccionado el color rojo.")
#    case "azul":
#        print("Has seleccionado el color azul.")
#    case "verde":
#        print("Has seleccionado el color verde.")
#    case _:
#        print("Color no disponible")

#
#
#
#
#



#####################################  Suma ################################################
def sumpro(numero1, numero2):
        suma = numero1 + numero2
        print(f"la suma del numero {numero1} con el numero {numero2} es {suma}")

num1 =int(input("Introduzca el primer numero: "))
num2 = int(input("Introduzca el segundo numero: "))

sumpro(num1, num2)

#####################################  Resta ################################################
def restpro(numero1, numero2):
        resta = numero1 - numero2
        print(f"la resta del numero {numero1} menos el numero {numero2} es {resta}")

num1 =int(input("Introduzca el primer numero: "))
num2 = int(input("Introduzca el segundo numero: "))

restpro(num1, num2)

#####################################  Division ################################################
def divpro(numero1, numero2):
        div = numero1 / numero2
        print(f"la division del numero {numero1} entre el numero {numero2} es {div}")

num1 =int(input("Introduzca el primer numero: "))
num2 = int(input("Introduzca el segundo numero: "))

divpro(num1, num2)