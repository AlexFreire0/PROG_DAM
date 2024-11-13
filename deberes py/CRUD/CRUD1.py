import mysql.connector as bbd
from datetime import date, time, datetime

conexion = bbd.connect(
        host="localhost",
        user="root",
        password="curso",
        database="SUPERMERCADO"
)

dt = datetime.now()


def crear_categoria(cursor, idcategoria, categoria):
    cursor.execute("INSERT INTO categoria (idcategoria, categoria) VALUES (%s, %s)", (idcategoria, categoria))
    conexion.commit()
    cursor.close()

def leer_categorias(cursor):
    cursor.execute("SELECT * FROM categoria")
    rows = cursor.fetchall()
    cursor.close()
    return rows

def actualizar_categoria(cursor, idcategoria, nueva_categoria):
    cursor.execute("UPDATE categoria SET categoria = %s WHERE idcategoria = %s", (nueva_categoria, idcategoria))
    conexion.commit()
    cursor.close()

def eliminar_categoria(cursor, idcategoria):
    cursor.execute("DELETE FROM categoria WHERE idcategoria = %s", (idcategoria,))
    conexion.commit()
    cursor.close()

def crear_pedido(cursor, idpedido, idcliente, fechapedido, fechaentrega):

    cursor.execute("INSERT INTO pedido (idpedido, idcliente, fechapedido, fechaentrega) VALUES (%s, %s, %s, %s)",
                   (idpedido, idcliente, fechapedido, fechaentrega))
    conexion.commit()
    cursor.close()

def leer_pedidos(cursor):

    cursor.execute("SELECT * FROM pedido")
    rows = cursor.fetchall()
    cursor.close()
    return rows

def actualizar_pedido(cursor, idpedido, idcliente, fechapedido, fechaentrega):
    cursor.execute("UPDATE pedido SET idcliente = %s, fechapedido = %s, fechaentrega = %s WHERE idpedido = %s",
                   (idcliente, fechapedido, fechaentrega, idpedido))
    conexion.commit()
    cursor.close()

def eliminar_pedido(cursor, idpedido):
    cursor.execute("DELETE FROM detalle WHERE idpedido = %s", (idpedido,))
    cursor.execute("DELETE FROM pedido WHERE idpedido = %s", (idpedido,))
    conexion.commit()
    cursor.close()

def create_detalle(cursor, idpedido, idproducto, precio, unidades, descuento):
    cursor.execute("INSERT INTO detalle (idpedido, idproducto, precio, unidades, descuento) VALUES (%s, %s, %s, %s, %s)",
                   (idpedido, idproducto, precio, unidades, descuento))
    conexion.commit()
    cursor.close()

def read_detalles(cursor, idpedido):
    cursor.execute("SELECT * FROM detalle WHERE idpedido = %s", (idpedido,))
    rows = cursor.fetchall()
    cursor.close()
    return rows

def update_detalle(cursor, idpedido, idproducto, precio, unidades, descuento):
    cursor.execute("UPDATE detalle SET precio = %s, unidades = %s, descuento = %s WHERE idpedido = %s AND idproducto = %s",
                   (precio, unidades, descuento, idpedido, idproducto))
    conexion.commit()
    cursor.close()

def delete_detalle(cursor, idpedido, idproducto):
    cursor.execute("DELETE FROM detalle WHERE idpedido = %s AND idproducto = %s", (idpedido, idproducto))
    conexion.commit()
    cursor.close()


def menu():
    global dt
    while True:
        cursor = conexion.cursor()
        print("\nSeleccione la tabla sobre la que desea operar:")
        print("\n1. Categoria")
        print("\n2. Pedido")
        print("\n3. Salir")
        
        choice = input("\nIngrese su opción: ")
        
        if choice == "1":
            print("\nOperaciones CRUD para Categoria:")
            print("\n1. Crear Categoria")
            print("\n2. Leer Categorias")
            print("\n3. Actualizar Categoria")
            print("\n4. Eliminar Categoria")
            eleccion = input("\nIngrese su opción: ")
           
            if eleccion == "1":
                idcategoria = int(input("Ingrese ID de la categoria: "))
                categoria = input("Ingrese el nombre de la categoria: ")
                crear_categoria(cursor, idcategoria, categoria)
                print("Categoria creada con éxito.")
                
            elif eleccion == "2":
                categorias = leer_categorias(cursor)
                for categoria in categorias:
                    print(categoria)
                    
            elif eleccion == "3":
                idcategoria = int(input("Ingrese ID de la categoria a actualizar: "))
                nueva_categoria = input("Ingrese el nuevo nombre de la categoria: ")
                actualizar_categoria(cursor, idcategoria, nueva_categoria)
                print("Categoria actualizada con éxito.")
                
            elif eleccion == "4":
                idcategoria = int(input("Ingrese ID de la categoria a eliminar: "))
                eliminar_categoria(cursor, idcategoria)
                print("Categoria eliminada con éxito.")
        elif choice == "2":
            print("\nOperaciones CRUD para Pedido y Detalles:")
            print("\n1. Crear Pedido")
            print("\n2. Leer Pedidos")
            print("\n3. Actualizar Pedido")
            print("\n4. Eliminar Pedido")
            eleccion = input("\nIngrese su opción: ")
          
            if eleccion == "1":
                idpedido = int(input("Ingrese ID del pedido: "))
                idcliente = input("Ingrese ID del cliente: ")
                fechapedido = f"{dt.year}-{dt.month}-{dt.day}"
                fechaentrega = f"{dt.year}-{dt.month}-{dt.day + 7}"
                crear_pedido(cursor, idpedido, idcliente, fechapedido, fechaentrega)
                print("Pedido creado con éxito.")
                
            elif eleccion == "2":
                pedidos = leer_pedidos(cursor)
                for pedido in pedidos:
                    print(pedido)
                    
            elif eleccion == "3":
                idpedido = int(input("Ingrese ID del pedido a actualizar: "))
                idcliente = input("Ingrese el nuevo ID del cliente: ")
                fechapedido = input("Ingrese la nueva fecha del pedido (YYYY-MM-DD): ")
                fechaentrega = input("Ingrese la nueva fecha de entrega (YYYY-MM-DD): ")
                fechapedido = f"{dt.year}-{dt.month}-{dt.day}"
                fechaentrega = f"{dt.year}-{dt.month}-{dt.day + 7}"
                actualizar_pedido(cursor, idpedido, idcliente, fechapedido, fechaentrega)
                print("Pedido actualizado con éxito.")
                
            elif eleccion == "4":
                idpedido = int(input("Ingrese ID del pedido a eliminar: "))
                eliminar_pedido(cursor, idpedido)
                print("Pedido eliminado con éxito.")
                
            elif eleccion == "5":
                idpedido = int(input("Ingrese ID del pedido: "))
                idproducto = int(input("Ingrese ID del producto: "))
                precio = float(input("Ingrese el precio: "))
                unidades = int(input("Ingrese el número de unidades: "))
                descuento = float(input("Ingrese el descuento: "))
                create_detalle(cursor, idpedido, idproducto, precio, unidades, descuento)
                print("Detalle creado con éxito.")

        elif choice == "3":
            print("\nSaliendo del programa.")
            conexion.close()
            break
        else:
            print("\nOpción no válida. Intente de nuevo.")
            
            
menu()
