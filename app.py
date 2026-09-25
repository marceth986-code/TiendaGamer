import json

ARCHIVO = "datos.json"


# =========================
# CARGAR Y GUARDAR DATOS
# =========================

def cargar_datos():
    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_datos(productos):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(productos, archivo, indent=4, ensure_ascii=False)


# =========================
# MOSTRAR PRODUCTOS
# =========================

def mostrar_productos(productos):
    print("\n===== PRODUCTOS =====")

    if len(productos) == 0:
        print("No hay productos cargados.")
        return

    for producto in productos:
        print(
            f'ID: {producto["id"]} | '
            f'Nombre: {producto["nombre"]} | '
            f'Categoría: {producto["categoria"]} | '
            f'Precio: ${producto["precio"]} | '
            f'Stock: {producto["stock"]}'
        )


# =========================
# AGREGAR PRODUCTO
# =========================

def agregar_producto(productos):
    print("\n===== AGREGAR PRODUCTO =====")

    nombre = input("Nombre: ")
    categoria = input("Categoría: ")

    try:
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))
    except ValueError:
        print("Precio o stock inválido.")
        return

    if len(productos) == 0:
        nuevo_id = 1
    else:
        nuevo_id = max(producto["id"] for producto in productos) + 1

    nuevo_producto = {
        "id": nuevo_id,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock
    }

    productos.append(nuevo_producto)
    guardar_datos(productos)

    print("Producto agregado correctamente.")


# =========================
# BUSCAR PRODUCTO
# =========================

def buscar_producto(productos):
    print("\n===== BUSCAR PRODUCTO =====")

    nombre_buscado = input("Ingresá el nombre del producto: ").lower()

    encontrado = False

    for producto in productos:
        if nombre_buscado in producto["nombre"].lower():
            print(
                f'ID: {producto["id"]} | '
                f'Nombre: {producto["nombre"]} | '
                f'Categoría: {producto["categoria"]} | '
                f'Precio: ${producto["precio"]} | '
                f'Stock: {producto["stock"]}'
            )

            encontrado = True

    if not encontrado:
        print("No se encontró ningún producto.")


# =========================
# MODIFICAR PRODUCTO
# =========================

def modificar_producto(productos):
    print("\n===== MODIFICAR PRODUCTO =====")

    mostrar_productos(productos)

    try:
        id_producto = int(input("Ingresá el ID del producto: "))
    except ValueError:
        print("El ID debe ser un número.")
        return

    for producto in productos:
        if producto["id"] == id_producto:

            print("\nDejá vacío un dato si no querés modificarlo.")

            nuevo_nombre = input(
                f'Nombre ({producto["nombre"]}): '
            )

            nueva_categoria = input(
                f'Categoría ({producto["categoria"]}): '
            )

            nuevo_precio = input(
                f'Precio ({producto["precio"]}): '
            )

            nuevo_stock = input(
                f'Stock ({producto["stock"]}): '
            )

            if nuevo_nombre != "":
                producto["nombre"] = nuevo_nombre

            if nueva_categoria != "":
                producto["categoria"] = nueva_categoria

            if nuevo_precio != "":
                try:
                    producto["precio"] = float(nuevo_precio)
                except ValueError:
                    print("Precio inválido.")
                    return

            if nuevo_stock != "":
                try:
                    producto["stock"] = int(nuevo_stock)
                except ValueError:
                    print("Stock inválido.")
                    return

            guardar_datos(productos)

            print("Producto modificado correctamente.")
            return

    print("No se encontró un producto con ese ID.")


# =========================
# ELIMINAR PRODUCTO
# =========================

def eliminar_producto(productos):
    print("\n===== ELIMINAR PRODUCTO =====")

    mostrar_productos(productos)

    try:
        id_producto = int(
            input("Ingresá el ID del producto que querés eliminar: ")
        )
    except ValueError:
        print("El ID debe ser un número.")
        return

    for producto in productos:
        if producto["id"] == id_producto:

            productos.remove(producto)
            guardar_datos(productos)

            print("Producto eliminado correctamente.")
            return

    print("No se encontró un producto con ese ID.")


# =========================
# ORDENAR PRODUCTOS
# =========================

def ordenar_productos(productos):
    print("\n===== ORDENAR PRODUCTOS =====")
    print("1. Por nombre")
    print("2. Por precio de menor a mayor")
    print("3. Por precio de mayor a menor")
    print("4. Por stock")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        productos.sort(key=lambda producto: producto["nombre"].lower())

    elif opcion == "2":
        productos.sort(key=lambda producto: producto["precio"])

    elif opcion == "3":
        productos.sort(
            key=lambda producto: producto["precio"],
            reverse=True
        )

    elif opcion == "4":
        productos.sort(key=lambda producto: producto["stock"])

    else:
        print("Opción inválida.")
        return

    guardar_datos(productos)
    print("Productos ordenados correctamente.")


# =========================
# FILTRAR POR CATEGORÍA
# =========================

def filtrar_categoria(productos):
    print("\n===== FILTRAR POR CATEGORÍA =====")

    categoria_buscada = input(
        "Ingresá la categoría: "
    ).lower()

    encontrados = False

    for producto in productos:
        if categoria_buscada in producto["categoria"].lower():

            print(
                f'ID: {producto["id"]} | '
                f'Nombre: {producto["nombre"]} | '
                f'Categoría: {producto["categoria"]} | '
                f'Precio: ${producto["precio"]} | '
                f'Stock: {producto["stock"]}'
            )

            encontrados = True

    if not encontrados:
        print("No hay productos de esa categoría.")


# =========================
# MENÚ PRINCIPAL
# =========================

productos = cargar_datos()

while True:

    print("\n==============================")
    print("       TIENDAGAMER")
    print("==============================")

    print("1. Mostrar productos")
    print("2. Agregar producto")
    print("3. Buscar producto")
    print("4. Modificar producto")
    print("5. Eliminar producto")
    print("6. Ordenar productos")
    print("7. Filtrar por categoría")
    print("8. Salir")

    opcion = input("\nElegí una opción: ")

    if opcion == "1":
        mostrar_productos(productos)
        input("\nPresioná ENTER para volver al menú...")

    elif opcion == "2":
        agregar_producto(productos)
        input("\nPresioná ENTER para volver al menú...")

    elif opcion == "3":
        buscar_producto(productos)
        input("\nPresioná ENTER para volver al menú...")

    elif opcion == "4":
        modificar_producto(productos)
        input("\nPresioná ENTER para volver al menú...")

    elif opcion == "5":
        eliminar_producto(productos)
        input("\nPresioná ENTER para volver al menú...")

    elif opcion == "6":
        ordenar_productos(productos)
        input("\nPresioná ENTER para volver al menú...")

    elif opcion == "7":
        filtrar_categoria(productos)
        input("\nPresioná ENTER para volver al menú...")

    elif opcion == "8":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")
        input("\nPresioná ENTER para volver al menú...")