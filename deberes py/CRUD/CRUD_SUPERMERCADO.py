import mysql.connector
from datetime import datetime

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="curso",
    database="SUPERMERCADO"
)

cursor = conexion.cursor()

def mostrar_menu():
    print("\nMenú principal:")
    print("1. Categorías")
    print("2. Pedidos")
    print("3. Salir")
    return int(input("Selecciona una opción: "))

def mostrar_submenu():
    print("\nOperaciones CRUD:")
    print("1. Crear")
    print("2. Leer")
    print("3. Actualizar")
    print("4. Eliminar")
    return int(input("Selecciona una operación: "))

def crud_categorias(operacion):
    if operacion == 1:
        idcategoria = int(input("ID de la categoría: "))
        categoria = input("Nombre de la categoría: ")
        cursor.execute("INSERT INTO categoria (idcategoria, categoria) VALUES (%s, %s)", (idcategoria, categoria))
        conexion.commit()
        print("Categoría creada.")
    elif operacion == 2:
        cursor.execute("SELECT * FROM categoria")
        for row in cursor.fetchall():
            print(row)
    elif operacion == 3:
        idcategoria = int(input("ID de la categoría a actualizar: "))
        nuevo_nombre = input("Nuevo nombre de la categoría: ")
        cursor.execute("UPDATE categoria SET categoria = %s WHERE idcategoria = %s", (nuevo_nombre, idcategoria))
        conexion.commit()
        print("Categoría actualizada.")
    elif operacion == 4:
        idcategoria = int(input("ID de la categoría a eliminar: "))
        cursor.execute("DELETE FROM categoria WHERE idcategoria = %s", (idcategoria,))
        conexion.commit()
        print("Categoría eliminada.")

def crud_pedidos(operacion):
    if operacion == 1:
        idpedido = int(input("ID del pedido: "))
        idcliente = input("ID del cliente: ")
        fechapedido = input("Fecha del pedido (YYYY-MM-DD): ")
        fechaentrega = input("Fecha de entrega (YYYY-MM-DD): ")
        cursor.execute(
            "INSERT INTO pedido (idpedido, idcliente, fechapedido, fechaentrega) VALUES (%s, %s, %s, %s)",
            (idpedido, idcliente, fechapedido, fechaentrega)
        )
        conexion.commit()
        print("Pedido creado.")
    elif operacion == 2:
        cursor.execute("SELECT * FROM pedido")
        for row in cursor.fetchall():
            print(row)
    elif operacion == 3:
        idpedido = int(input("ID del pedido a actualizar: "))
        nueva_fecha_entrega = input("Nueva fecha de entrega (YYYY-MM-DD): ")
        cursor.execute("UPDATE pedido SET fechaentrega = %s WHERE idpedido = %s", (nueva_fecha_entrega, idpedido))
        conexion.commit()
        print("Pedido actualizado.")
    elif operacion == 4:
        idpedido = int(input("ID del pedido a eliminar: "))
        cursor.execute("DELETE FROM detalle WHERE idpedido = %s", (idpedido,))  # Borramos detalles primero
        cursor.execute("DELETE FROM pedido WHERE idpedido = %s", (idpedido,))
        conexion.commit()
        print("Pedido eliminado.")

while True:
    opcion_tabla = mostrar_menu()
    if opcion_tabla == 1:
        operacion = mostrar_submenu()
        crud_categorias(operacion)
    elif opcion_tabla == 2:
        operacion = mostrar_submenu()
        crud_pedidos(operacion)
    elif opcion_tabla == 3:
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida.")

conexion.close()
