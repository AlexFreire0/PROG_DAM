from datetime import date, time, datetime
dt = datetime.now()
clientes = {
    "root": {
        "nombre": "root",
        "direccion": "",
        "email": "",
        "Admin": True,
        "contraseña": "CampusFP"}}  
productos = {
    1: {"nombre": "Patatas", "precio": 8.0},
    2: {"nombre": "Zanahorias", "precio": 6.0},
    3: {"nombre": "Agua", "precio": 1.0},
}
numero_pedido = 0
pedidos = {}



def registrar_cliente():
    id_cliente = input("Ingrese un ID único para el cliente: ")
    if id_cliente in clientes:
        print("Este ID ya existe. Intente con otro.")
        return

    admin = False
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    email = input("Ingrese el email del cliente: ")


    clientes[id_cliente] = {
        "nombre": nombre,
        "direccion": direccion,
        "email": email,
        "Admin": admin
    }
    print("\nCliente registrado con éxito.")
    mostrar_menu()
   
def ver_clientes():
    if not clientes :
        print("No hay clientes registrados aún")
    else:
        print("{:<15} {:<20} {:<30} {:<30}".format("ID Cliente", "Nombre", "Dirección", "Email"))
        for id_cliente, datos in clientes.items():
            print("{:<15} {:<20} {:<30} {:<30}".format(id_cliente, datos["nombre"], datos["direccion"], datos["email"]))
    mostrar_menu()
   
def buscar_cliente():
    cliente = input("Por favor, introduzca el ID del cliente: ")
    if cliente in clientes:
        datos = clientes[cliente]
        print("\nCliente:")
        print("{:<15} {:<20} {:<30} {:<30}".format("ID Cliente", "Nombre", "Dirección", "Email"))
        print("{:<15} {:<20} {:<30} {:<30}".format(cliente, datos["nombre"], datos["direccion"], datos["email"]))
    mostrar_menu()



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
            print(pedidos)
            break
        else:
            compra = int(compra)
            if compra in productos:
                productosencompra += [productos[compra]["nombre"]]
                valorescompra += [productos[compra]["precio"]]
    pedidos[numero_pedido] = {
        "producto": productosencompra,
        "precio": valorescompra,
        "Valor Total": sum(valorescompra),
        "Clienteid": idcliente,
        "fecha": dt.date().strftime("%Y-%m-%d")
        }                
    print(f"NºPedido: {numero_pedido}\nProductos: {productosencompra}\nFecha: {pedidos[numero_pedido]['fecha']}\nCliente: {idcliente}")
    mostrar_menu()

def seguimiento():
    print("Seleccione una de las opciones de seguimiento:")
    print("1 - Con Nº de pedido")
    print("2 - Con ID de cliente")
    eleccion = int(input("Por favor introduzca la opcion que desee: "))
    if eleccion == 1:
        Npedido = int(input("\n Introduzca el Nº de pedido: "))
        if Npedido in pedidos:
            print(f"\nNºpedido: {Npedido}\nProductos: {pedidos[Npedido]['producto']}\nFecha: {pedidos[numero_pedido]['fecha']}\n Cliente: {pedidos[numero_pedido]['Clienteid']} Valor Total: {pedidos[numero_pedido]['Valor Total']}€")
        else:
            print("\n Prodido no existente\n")
            mostrar_menu()
    elif eleccion == 2:

        Clienteid = input("\n Por favor introduzca su ID de cliente: ")
        if Clienteid not in clientes:
            print("\nEl cliente no existe")
            return
        for Npedido, detalles in pedidos.items():
            if detalles['Clienteid'] == Clienteid:
                print(f"\nNº Pedido: {Npedido}\nProductos: {detalles['producto']}\nFecha: {detalles['fecha']}\nValor Total: {detalles['Valor Total']}€")
                encontrado = True
        if encontrado == False:
            print("No se han encontrado pedidos de este cliente")
    else: 
        print("Por favor introduzca una opcion valida")
        seguimiento()    
      
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
            print("Error, indique una opcion valida")
            mostrar_menu()
mostrar_menu()