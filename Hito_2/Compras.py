from datetime import date, time, datetime
dt = datetime.now()
contrasena_admin = "CampusFP2425"
clientes = {    # Diccionario vacío para almacenar clientes
}  
productos = {
    1: {"nombre": "Patatas", "precio": 8.0},
    2: {"nombre": "Zanahorias", "precio": 6.0},
    3: {"nombre": "Agua", "precio": 1.0},
}
numero_pedido = 0 # Contador para los pedidos
pedidos = {} # Diccionario para almacenar los pedidos



def registrar_cliente():
    while True:
        id_cliente = input("Ingrese un ID único para el cliente: ")
        if id_cliente in clientes:
            print("Este ID ya existe. Intente con otro.")
        else:
            break
    # pedimos toda la informacion
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    email = input("Ingrese el email del cliente: ")

    # Lo registramos al cliente en el diccionario
    clientes[id_cliente] = {
        "nombre": nombre,
        "direccion": direccion,
        "email": email,
    }
    print("\nCliente registrado con éxito.")
    mostrar_menu()
   #Hacemos la funcion en la que a partir de demostrar tener la contraseña del admin podamos ver a todos los clientes y su respectiva información.
def ver_clientes():
    confirmacion = input("Introduzca la contraseña de admin para poder realizar esta acción: ")
    if confirmacion == contrasena_admin:
        if not clientes :
            print("No hay clientes registrados aún")
        else:
            print("\n{:<15} {:<20} {:<30} {:<30}".format("ID Cliente", "Nombre", "Dirección", "Email"))
            for id_cliente, datos in clientes.items():
                print("{:<15} {:<20} {:<30} {:<30}".format(id_cliente, datos["nombre"], datos["direccion"], datos["email"]))
    mostrar_menu()
   # En esta funcion al igual q en ver clientes tendremos q introducir el codigo admin y el cliente del que deseemos ver la informacion
def buscar_cliente():
    confirmacion = input("Introduzca la contraseña de admin para poder realizar esta acción: ")
    if confirmacion == contrasena_admin:
        cliente = input("Por favor, introduzca el ID del cliente: ")
        if cliente in clientes:
            datos = clientes[cliente]
            print("\nCliente:")
            #Mostramos los clientes con forma
            print("{:<15} {:<20} {:<30} {:<30}".format("ID Cliente", "Nombre", "Dirección", "Email"))
            print("{:<15} {:<20} {:<30} {:<30}".format(cliente, datos["nombre"], datos["direccion"], datos["email"]))
    mostrar_menu()


    # Para realizar la compra necesitaremos meter toda la informacion en el diccionario global de pedidos y despues ligarlo de alguna manera con el cliente como se ha hecho aqui.
def realizar_compra():
    productosencompra = []
    valorescompra = []
    idcliente = input("Por favor, introduzca su ID: ")
    global numero_pedido
    if idcliente not in clientes:
        print("El ID de cliente no está registrado. Por favor, registre al cliente primero.")
        mostrar_menu()
        return
    numero_pedido += 1
    print("\n--------Productos disponibles---------")
    for producto, datos in productos.items():
        print("{:<10} {:<20} {:<30}".format(producto, datos["nombre"], datos["precio"]))
    while True:
       
        compra = input("Indique el numero del producto que desea comprar(si has terminado escribe 'fin'): ")
        if compra.lower() == 'fin':
            if comprado == True:
                print(pedidos)
            else:
                print("No ha comprado nada")
            break
        else:
            compra = int(compra)
            if compra in productos:
                #Meteremos el valor de los productos y los productos en listas.
                productosencompra += [productos[compra]["nombre"]]
                valorescompra += [productos[compra]["precio"]]
                comprado = True
    #Tras haber metido en listas o haber recogido toda la información, meteremos esto en el diccionario de la compra con su respectivo nº de pedido.
    pedidos[numero_pedido] = {
        "producto": productosencompra,
        "precio": valorescompra,
        "Valor Total": sum(valorescompra),
        "Clienteid": idcliente,
        "fecha": dt.date().strftime("%Y-%m-%d")
        } 
    #Tras realizar la compra mostraremos la compra realizada justo ahora.               
    print(f"NºPedido: {numero_pedido}\nProductos: {productosencompra}\nFecha: {pedidos[numero_pedido]['fecha']}\nCliente: {idcliente}")
    mostrar_menu()
    # En esta funcion seguiremos los pedidos de dos formas diferentes, 1 de estas es mediante el Nº del pedido y la otra mediante el ID cliente
def seguimiento():
    print("Seleccione una de las opciones de seguimiento:")
    print("1 - Con Nº de pedido")
    print("2 - Con ID de cliente")
    eleccion = int(input("Por favor introduzca la opcion que desee: "))
    if eleccion == 1:
        Npedido = int(input("\n Introduzca el Nº de pedido: "))
        if Npedido in pedidos:
            #Imprimimos el pedido de manera que el usuario pueda entender de manera adecuada el contenido.
            print(f"\nNºpedido: {Npedido}\nProductos: {pedidos[Npedido]['producto']}\nFecha: {pedidos[Npedido]['fecha']}\n Cliente: {pedidos[Npedido]['Clienteid']} Valor Total: {pedidos[Npedido]['Valor Total']}€")
        else:
            print("\n Pedido no existente\n")
            mostrar_menu()
    elif eleccion == 2:

        Clienteid = input("\n Por favor introduzca su ID de cliente: ")
        if Clienteid not in clientes:
            print("\nEl cliente no existe")
            mostrar_menu()
            return
        for Npedido, detalles in pedidos.items():
            if detalles['Clienteid'] == Clienteid:
                print(f"\nNº Pedido: {Npedido}\nProductos: {detalles['producto']}\nFecha: {detalles['fecha']}\nValor Total: {detalles['Valor Total']}€")
                encontrado = True
        if encontrado == False:
            print("No se han encontrado pedidos de este cliente")
    else: 
        print("Por favor introduzca una opción válida")
        mostrar_menu()    
      # Esta es la funcion principal desde la cual podremos acceder a cualquiera de las funciones siendo un menu interactivo para el usuario.
def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Registrar Cliente")
    print("2. Ver Clientes")
    print("3. Buscar Cliente")
    print("4. Realizar Compra")
    print("5. Seguimiento de Pedido")
    print("6. Salir")
    Accion = int(input("Por favor indique la acción que desea realizar: "))
    match Accion:
        case 1:
            registrar_cliente()
        case 2:
            ver_clientes()
        case 3:
            buscar_cliente()
        case 4:
            realizar_compra()
        case 5:
            seguimiento()
        case 6:
            return
        case _:
            print("Error, indique una opcion válida")
            mostrar_menu()
# Llamamos a la funcion principal del menú
mostrar_menu()