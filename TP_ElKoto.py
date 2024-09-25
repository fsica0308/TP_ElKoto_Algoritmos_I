import json
from datetime import date, timedelta, datetime

'''
Anotaciones:

Promociones: 2x1 se guarda como texto "2x1", descuentos se guarda el % ej: 45, descuentos en x unidad se guarda ej: 25% en 2 unidad -> 252
Ademas las promociones son unicamente enteros. En caso de no tener promocion se indica con un 0.

JSON: Todo lo que se ingrese al JSON debe ingresarse sin tildes.
'''

def menu_principal():
    """ Funcion Menu Inicial, muestra un banner de bienvenida mediante un print, luego le da la opcion al usuario de seleccionar entre las opciones que cuenta el menu, 
        valida que la opcion elegida este entre las opciones dadas
    """
    
    banner = """
         _ ____  _                           _     _                 _____ _ _  __     _        _ 
        (_) __ )(_) ___ _ ____   _____ _ __ (_) __| | ___     __ _  | ____| | |/ /___ | |_ ___ | |
        | |  _ \| |/ _ \ '_ \ \ / / _ \ '_ \| |/ _` |/ _ \   / _` | |  _| | | ' // _ \| __/ _ \| |
        | | |_) | |  __/ | | \ V /  __/ | | | | (_| | (_) | | (_| | | |___| | . \ (_) | || (_) |_|
        |_|____/|_|\___|_| |_|\_/ \___|_| |_|_|\__,_|\___/   \__,_| |_____|_|_|\_\___/ \__\___/(_)
    """
    print(banner)
    
    print("Menu: \n\t1. Consultar informacion de productos \n\t2. ABM Productos \n\t3. Caja \n\t4. Estadisticas \n\t5. Salir")
    
    print()
    opcion = int(input("Opcion: "))
    while opcion < 1 or opcion > 5:
        opcion = int(input("Error. Ingrese una opcion correcta: "))
    
    return opcion

def leer_archivo():
    """
        Esta función abre el archivo 'productos.json' y carga su contenido.
        Si el archivo está vacío, muestra un mensaje indicando que no hay datos.
        Si todo sale bien, devuelve la información de los productos como un diccionario.
        En caso de que algo falle, muestra un mensaje de error.
    """
    
    try:    # Manejo de excepciones (si cualquier linea dentro de try lanza error, pasa al except)
        archivo = open("productos.json", "r")   # Abrimos el archivo productos.json en modo lectura y guardamos el objeto del archivo en archivo
        lineas_productos = archivo.read()   # Leemos todo el contenido de archivo y lo almacenamos en lineas_productos como una cadena de texto
        archivo.close() # Cerramos el archivo leido
    
        if len(lineas_productos) == 0:  # Si el archivo no contenia datos, entonces comprobamos que no sea una cadena vacia el resultado
            print("El archivo JSON está vacío o no contiene datos.")
            return
    
        productos = json.loads(lineas_productos)    # Convertimos el la cadena de texto del json en un diccionario o una lista dependiendo del archivo, y lo almacenamos en productos
        return productos    # Devolvemos el diccionario/lista obtenido
        
    except: # Si hubo alguna excepcion
        print("No se puede abrir el archivo productos")
        
def leer_archivo_ventas():
    """
        Esta función abre el archivo 'ventas.json' y carga su contenido.
        Si el archivo está vacío, muestra un mensaje indicando que no hay datos.
        Si todo sale bien, devuelve la información de las ventas como un diccionario.
        En caso de que algo falle, muestra un mensaje de error.
    """
    
    try:    # Manejo de excepciones (si cualquier linea dentro de try lanza error, pasa al except)
        archivo = open("ventas.json", "r")  # Abrimos el archivo ventas.json en modo lectura y guardamos el objeto del archivo en archivo
        lineas_ventas = archivo.read()  # Leemos todo el contenido de archivo y lo almacenamos en lineas_ventas como una cadena de texto
        archivo.close() # Cerramos el archivo leido
    
        if len(lineas_ventas) == 0: # Si el archivo no contenia datos, entonces comprobamos que no sea una cadena vacia el resultado
            print("El archivo JSON está vacío o no contiene datos.")
            return
    
        ventas = json.loads(lineas_ventas)  # Convertimos el la cadena de texto del json en un diccionario o una lista dependiendo del archivo, y lo almacenamos en ventas
        return ventas   # Devolvemos el diccionario/lista obtenido
        
    except: # Si hubo alguna excepcion
        print("No se puede abrir el archivo ventas")

def menu_info_productos():
    """
        Esta funcion muestra toda la información de los productos en formato de tabla.
        Además, permite buscar productos por nombre, marca o promoción.
        Luego de cada búsqueda, vuelve a mostrar el menú para hacer más consultas.
    """
    
    print()
    productos = leer_archivo()  # Llamamos funcion leer_archivo() y almacenamos el resultado en productos
    
    # Obtener las claves (nombres de las columnas) desde el primer elemento del JSON, ya que es una lista de diccionarios
    columnas = list(productos[0].keys())    # Convertimos la claves en una lista mediante list() para poder usar los nombre como columnas
    
    # Calcular el ancho de cada columna (máximo entre el largo del nombre de la clave y los valores)
    anchuras = {columna: len(columna) for columna in columnas}  # Creamos un diccionario anchuras donde las claves son los nombres de las columnas y los valores son la longitud del nombre de la columna
    for fila in productos:  # Por cada producto (diccionario) de la lista de productos
        for columna in columnas:    # Por cada columna del producto
            anchuras[columna] = max(anchuras[columna], len(str(fila[columna]))) # Calcula el mayor valor entre el ancho actual de la columna y la longitud del valor de la columna en la fila actual. Se convierte el valor con str() para poder usar len(). El objetivo es que cada columna tenga el ancho suficiente para contener los valores mas largos
    
    # Imprimir la cabecera y separador
    cabecera = " | ".join([columna.ljust(anchuras[columna]) for columna in columnas])   # Mediante (" | ".join) se crea una cadena de texto donde los nombres de las columnas estan separados por "|". Luego (columna.ljust(anchuras[columna])) alinea los nombres de las columnas a la izquierda, asegurandose de cada columna tenga el ancho maximo calculado en el paso previo
    separador = "-+-".join(['-' * anchuras[columna] for columna in columnas])   # Mediante ("-+-".join([...])) se crea una cadena de texto donde cada columna esta separada por "-+-". Luego ('-' * anchuras[columna]) genera una linea de "-" cuyo largo coincide con el ancho de cada columna
    print(cabecera)     # Imprimimos la cabecera
    print(separador)    # Imprimimos el separador
    
    # Imprimir las filas de datos
    for fila in productos:  # Por cada producto (fila) en la lista de productos
        linea = " | ".join([str(fila[columna]).ljust(anchuras[columna]) for columna in columnas])   # Mediante (" | ".join([...])) se crea una cadena de texto donde los valores de las columnas están separados por " | ". Luego (str(fila[columna]).ljust(anchuras[columna])) convierte cada valor de la columna en una cadena de texto y lo alinea a la izquierda, utilizando el ancho calculado para la columna
        print(linea)    # Se imprime cada fila de productos, alineando los valores de cada columna
      
    print()  
    print("Menu Consulta Producto: \n\t1. Busqueda por Nombre \n\t2. Busqueda por Marca \n\t3. Busqueda por Promocion \n\t4. Volver")   # Mostramos menu de consulta de productos
    
    print()
    opcion = int(input("Opcion: ")) 
    while opcion < 1 or opcion > 4:
        opcion = int(input("Error. Ingrese una opcion correcta: "))
        
    while opcion >= 1 and opcion <= 3:  # Si la opcion ingresada es 1, 2 o 3 (ya que con 4 volves al anterior menu)
        if opcion == 1:
            columna_busqueda = "nombre" # El campo del diccionario a filtrar es nombre
            valor_busqueda = input("Ingrese el Nombre del Producto: ")
            print()
            busqueda_filtrada(productos, columna_busqueda, valor_busqueda)  # Se filtran los productos segun el campo y nombre ingresado
        elif opcion == 2:
            columna_busqueda = "marca"  # El campo del diccionario a filtrar es marca
            valor_busqueda = input("Ingrese la Marca del Producto: ")
            print()
            busqueda_filtrada(productos, columna_busqueda, valor_busqueda)  # Se filtran los productos segun el campo y marca ingresada
        else:
            columna_busqueda = "promocion"  # El campo del diccionario a filtrar es promocion
            valor_busqueda = input("Ingrese la Promocion del Producto: ")
            print()
            busqueda_filtrada(productos, columna_busqueda, valor_busqueda)  # Se filtran los productos segun el campo y promocion ingresada
        
        # Volvemos a mostrar el menu las veces necesarias por si se requieren mas busquedas
        print()    
        print("Menu Consulta Producto: \n\t1. Busqueda por Nombre \n\t2. Busqueda por Marca \n\t3. Busqueda por Promocion \n\t4. Volver")   # Mostramos menu de consulta de productos
        print()
        opcion = int(input("Opcion: "))
        while opcion < 1 or opcion > 4:
            opcion = int(input("Error. Ingrese una opcion correcta: "))     
    else:   # Selecciono volver
        return
             
def busqueda_filtrada(productos, columna_busqueda, valor_busqueda):
    """
        Esta funcion filtra los productos según la columna y el valor que elijas (nombre, marca o promoción).
        Si no encuentra nada, te avisa. Si encuentra, te muestra los resultados en una tabla.
    """

    # Obtener las claves (nombres de las columnas) desde el primer elemento del JSON, ya que es una lista de diccionarios
    columnas = list(productos[0].keys())    # Convertimos la claves en una lista mediante list() para poder usar los nombre como columnas

    # Filtrar los datos según la columna y el valor de búsqueda
    datos_filtrados = [fila for fila in productos if valor_busqueda.lower() in str(fila.get(columna_busqueda, '')).lower()] # Creamos una lista datos_filtrado por comprension con todos los productos que cumplan el criterio de bsuqueda. Por cada producto, transformamos el valor a buscar a minusculas y mediante (fila.get(columna_busqueda, '')) buscamos si se encuentra la columna deseada como clave del diccionario producto, luego lo transformamos a minusculas y a str() para hacer la comparacion

    # Verificar si hay resultados
    if len(datos_filtrados) == 0:   # Si esta vacio
        print(f"No se encontraron resultados para '{valor_busqueda}' en la columna '{columna_busqueda}'.")
        return

    # Calcular el ancho de cada columna (máximo entre el largo del nombre de la clave y los valores)
    anchuras = {columna: len(columna) for columna in columnas}  # Creamos un diccionario anchuras donde las claves son los nombres de las columnas y los valores son la longitud del nombre de la columna
    for fila in datos_filtrados:    # Por cada producto (diccionario) de la lista datos_filtrados
        for columna in columnas:    # Por cada columna del producto
            anchuras[columna] = max(anchuras[columna], len(str(fila[columna]))) # Calcula el mayor valor entre el ancho actual de la columna y la longitud del valor de la columna en la fila actual. Se convierte el valor con str() para poder usar len(). El objetivo es que cada columna tenga el ancho suficiente para contener los valores mas largos

    # Imprimir la cabecera y separador
    cabecera = " | ".join([columna.ljust(anchuras[columna]) for columna in columnas])   # Mediante (" | ".join) se crea una cadena de texto donde los nombres de las columnas estan separados por "|". Luego (columna.ljust(anchuras[columna])) alinea los nombres de las columnas a la izquierda, asegurandose de cada columna tenga el ancho maximo calculado en el paso previo
    separador = "-+-".join(['-' * anchuras[columna] for columna in columnas])   # Mediante ("-+-".join([...])) se crea una cadena de texto donde cada columna esta separada por "-+-". Luego ('-' * anchuras[columna]) genera una linea de "-" cuyo largo coincide con el ancho de cada columna
    print(cabecera)     # Imprimimos la cabecera
    print(separador)    # Imprimimos el separador

    # Imprimir las filas de datos filtradas
    for fila in datos_filtrados:    # Por cada producto (fila) en la lista datos_filtrados
        linea = " | ".join([str(fila[columna]).ljust(anchuras[columna]) for columna in columnas])   # Mediante (" | ".join([...])) se crea una cadena de texto donde los valores de las columnas están separados por " | ". Luego (str(fila[columna]).ljust(anchuras[columna])) convierte cada valor de la columna en una cadena de texto y lo alinea a la izquierda, utilizando el ancho calculado para la columna
        print(linea)    # Se imprime cada fila de productos, alineando los valores de cada columna

def menu_abm_productos():
    """
        Esta funcion muestra un menú donde puedes agregar, eliminar o modificar productos.
        Te pide elegir una opción y ejecuta la función correspondiente (alta, baja o modificación).
    """
    
    print()
    print("Menu ABM Productos: \n\t1. Alta Producto \n\t2. Baja Producto \n\t3. Modificacion Producto \n\t4. Volver")   # Mostramos menu abm productos
    
    print()
    opcion = int(input("Opcion: "))
    while opcion < 1 or opcion > 4:
        opcion = int(input("Error. Ingrese una opcion correcta: "))
        
    productos = leer_archivo()
        
    while opcion >= 1 and opcion <= 3:  # Si la opcion ingresada es 1, 2 o 3 (ya que con 4 volves al anterior menu)
        if opcion == 1:
            alta_producto(productos)    # Llamamos y hacemos alta de producto
        elif opcion == 2:
            baja_producto(productos)    # Llamamos y hacemos baja de producto
        else:
            modificar_producto(productos)   # Llamamos y hacemos modificacion de producto
            
        # Volvemos a mostrar el menu las veces necesarias por si se requieren mas abm productos
        print("Menu ABM Productos: \n\t1. Alta Producto \n\t2. Baja Producto \n\t3. Modificacion Producto \n\t4. Volver")   # Mostramos menu abm productos
        print()
        opcion = int(input("Opcion: "))
        while opcion < 1 or opcion > 4:
            opcion = int(input("Error. Ingrese una opcion correcta: "))     
    else:   # Selecciono volver
        return



#DIVIDO ESTA FUNCION EN 4, BUSQUEDA ALTA, BAJA, MODIFICACION Y CAJA, POR LO QUE PIDIO LA PROFE EN EL PARCIAL
#DESPUES BORRAR ESTA FUNCION O COMENTAR
def busqueda_producto(productos, modo):
    """
        Esta funcion integra la busqueda de porductos de las funciones alta, baja, mod y caja. Segun las necesidades de cada una de ellas.
    """
    
    if modo == "alta":  # Si el modo es alta, se realizara la busqueda del producto para corroborar que no exista antes de dar de alta
        encontrado = False  # Variable booleana que comienza default en False hasta encontrar el producto
        
        nombre = input("\tIngrese el nombre: ")
        marca = input("\tIngrese la marca: ")
        
        # Recorrer la lista y verificar si algún producto tiene el nombre y marca buscado
        for producto in productos:  # Por cada producto
            if producto['nombre'].lower() == nombre.lower() and producto['marca'].lower() == marca.lower(): # Si el valor de la clave nombre es igual al nombre ingresado por el usuario, y al mismo tiempo la marca es la misma que la ingresada, (todo en minusculas)
                encontrado = True   # Se encontro el producto
                break   # Se deja de buscar
        
        while encontrado:   # Mientras se haya encontrado el producto, se continuara buscando y pidiendo al usuario los datos, hasta que ya no se encuentre y poder dar el alta
            print("El producto ya existe, ingrese otro por favor: ")
            nombre = input("\tIngrese el nombre: ")
            marca = input("\tIngrese la marca: ")
            encontrado = False  # Se vuelve a poner en False para volver a buscar
            for producto in productos:
                if producto['nombre'].lower() == nombre.lower() and producto['marca'].lower() == marca.lower():
                    encontrado = True
                    break
                
        return nombre, marca    # Devolvemos el nombre y la marca
                
    elif modo == "modificacion":    # Si el modo es modificacion, se realizara la busqueda del producto para corroborar que exista y poder modificarlo
        idProducto = int(input("\tIngrese el id del producto que desea modificar: "))
        encontrado = None   # Variable default en None ya que aca guardaremos el diccionario del producto una vez encontrado

        # Recorrer la lista y verificar si algún producto tiene el id del producto que se requiere modificar
        for producto in productos:  # Por cada producto
            if producto['id'] == idProducto :   # Si el valor de la clave id es igual al id ingresado
                encontrado = producto   # Se guarda el producto en encontrado
                break   # Se deja de buscar
        
        while encontrado is None:   # Mientras no se haya encontrado el producto, se continuara buscando y pidiendo al usuario un id, hasta encontrar un producto y poder modificarlo
            print(f"El producto con id {idProducto} no existe")
            idProducto = int(input("\tIngrese el id del producto que desea modificar: "))
            encontrado = None   # Se vuelve a poner en None para volver a buscar
            for producto in productos:
                if producto['id'] == idProducto :
                    encontrado = producto
                    break
                    
        return idProducto, encontrado   # Devolvemos el id ingresado y el producto encontrado
        
    elif modo == "baja":    # Si el modo es baja, se realizara la busqueda del producto para corroborar que exista y poder eliminarlo
        idProducto = int(input("\tIngrese el id del producto que desea eliminar: "))
        encontrado = False  # Variable booleana que comienza default en False hasta encontrar el producto

        # Recorrer la lista y verificar si algún producto tiene el id del producto que se requiere eliminar
        for producto in productos:  # Por cada producto
            if producto['id'] == idProducto :   # Si el valor de la clave id es igual al id ingresado
                encontrado = True   # Se encontro el producto
                break   # Se deja de buscar    
            
        while not encontrado:   # Mientras no se haya encontrado el producto, se continuara buscando y pidiendo al usuario el id, hasta que se encuentre y poder dar la baja
            print(f"El producto con id {idProducto} no existe")
            idProducto = int(input("\tIngrese el id del producto que desea eliminar: "))
            encontrado = False  # Se vuelve a poner en False para volver a buscar
            for producto in productos:
                if producto['id'] == idProducto :
                    encontrado = True
                    break
                
        return idProducto, encontrado   # Devolvemos el id y el producto encontrado
    
    else:   # Si el modo es caja, se realizara la busqueda del producto para corroborar que exista y poder tomar y calcular sus datos
        idProducto = int(input("\tIngrese el id del producto: "))
        encontrado = None   # Variable default en None ya que aca guardaremos el diccionario del producto una vez encontrado

        # Recorrer la lista y verificar si algún producto tiene el id del producto que se requiere vender
        for producto in productos:  # Por cada producto  
            if producto['id'] == idProducto :   # Si el valor de la clave id es igual al id ingresado
                encontrado = producto   # Guardamos el producto encontrado
                break   # Se deja de buscar 
        
        while encontrado is None:   # Mientras no se haya encontrado el producto, se continuara buscando y pidiendo al usuario un id, hasta encontrar un producto y poder continuar la venta
            print(f"El producto con id {idProducto} no existe")
            idProducto = int(input("\tIngrese el id del producto a vender: "))
            encontrado = None   # Se vuelve a poner en None para volver a buscar
            for producto in productos:
                if producto['id'] == idProducto :
                    encontrado = producto
                    break
                    
        return idProducto, encontrado   # Devolvemos el id y el producto encontrado

#Declaro las 4 funciones por separado
def busqueda_producto_alta(productos):
    encontrado = False  # Variable booleana que comienza default en False hasta encontrar el producto
        
    nombre = input("\tIngrese el nombre: ")
    marca = input("\tIngrese la marca: ")
        
    # Recorrer la lista y verificar si algún producto tiene el nombre y marca buscado
    for producto in productos:  # Por cada producto
        if producto['nombre'].lower() == nombre.lower() and producto['marca'].lower() == marca.lower(): # Si el valor de la clave nombre es igual al nombre ingresado por el usuario, y al mismo tiempo la marca es la misma que la ingresada, (todo en minusculas)
            encontrado = True   # Se encontro el producto
            break   # Se deja de buscar
    
    while encontrado:   # Mientras se haya encontrado el producto, se continuara buscando y pidiendo al usuario los datos, hasta que ya no se encuentre y poder dar el alta
        print("El producto ya existe, ingrese otro por favor: ")
        nombre = input("\tIngrese el nombre: ")
        marca = input("\tIngrese la marca: ")
        encontrado = False  # Se vuelve a poner en False para volver a buscar
        for producto in productos:
            if producto['nombre'].lower() == nombre.lower() and producto['marca'].lower() == marca.lower():
                encontrado = True
                break
                
    return nombre, marca    # Devolvemos el nombre y la marca


def busqueda_producto_baja(productos):
    idProducto = int(input("\tIngrese el id del producto que desea eliminar: "))
    encontrado = False  # Variable booleana que comienza default en False hasta encontrar el producto

    # Recorrer la lista y verificar si algún producto tiene el id del producto que se requiere eliminar
    for producto in productos:  # Por cada producto
        if producto['id'] == idProducto :   # Si el valor de la clave id es igual al id ingresado
            encontrado = True   # Se encontro el producto
            break   # Se deja de buscar    
            
    while not encontrado:   # Mientras no se haya encontrado el producto, se continuara buscando y pidiendo al usuario el id, hasta que se encuentre y poder dar la baja
        print(f"El producto con id {idProducto} no existe")
        idProducto = int(input("\tIngrese el id del producto que desea eliminar: "))
        encontrado = False  # Se vuelve a poner en False para volver a buscar
        for producto in productos:
            if producto['id'] == idProducto :
                encontrado = True
                break
                
    return idProducto, encontrado   # Devolvemos el id y el producto encontrado

def busqueda_producto_modificacion(productos):
    idProducto = int(input("\tIngrese el id del producto que desea modificar: "))
    encontrado = None   # Variable default en None ya que aca guardaremos el diccionario del producto una vez encontrado

    # Recorrer la lista y verificar si algún producto tiene el id del producto que se requiere modificar
    for producto in productos:  # Por cada producto
        if producto['id'] == idProducto :   # Si el valor de la clave id es igual al id ingresado
            encontrado = producto   # Se guarda el producto en encontrado
            break   # Se deja de buscar
        
    while encontrado is None:   # Mientras no se haya encontrado el producto, se continuara buscando y pidiendo al usuario un id, hasta encontrar un producto y poder modificarlo
        print(f"El producto con id {idProducto} no existe")
        idProducto = int(input("\tIngrese el id del producto que desea modificar: "))
        encontrado = None   # Se vuelve a poner en None para volver a buscar
        for producto in productos:
            if producto['id'] == idProducto :
                encontrado = producto
                break
                    
    return idProducto, encontrado   # Devolvemos el id ingresado y el producto encontrado

def busqueda_producto_caja(productos):
    idProducto = int(input("\tIngrese el id del producto: "))
    encontrado = None   # Variable default en None ya que aca guardaremos el diccionario del producto una vez encontrado

    # Recorrer la lista y verificar si algún producto tiene el id del producto que se requiere vender
    for producto in productos:  # Por cada producto  
        if producto['id'] == idProducto :   # Si el valor de la clave id es igual al id ingresado
            encontrado = producto   # Guardamos el producto encontrado
            break   # Se deja de buscar 
        
    while encontrado is None:   # Mientras no se haya encontrado el producto, se continuara buscando y pidiendo al usuario un id, hasta encontrar un producto y poder continuar la venta
        print(f"El producto con id {idProducto} no existe")
        idProducto = int(input("\tIngrese el id del producto a vender: "))
        encontrado = None   # Se vuelve a poner en None para volver a buscar
        for producto in productos:
            if producto['id'] == idProducto :
                encontrado = producto
                break
                    
    return idProducto, encontrado   # Devolvemos el id y el producto encontrado  


def alta_producto(productos):
    """
        Esta funcion agrega un nuevo producto pidiendo los datos como nombre, marca, precio, ubicación y stock.
        Además, te da la opción de agregar una promoción al producto.
        Guarda el producto nuevo en el archivo JSON.
    """
    
    print("Datos del Producto: ")
    # Obtener el diccionario con el valor máximo de "id"
    maximo_id = max(productos, key=obtener_id)  # Obtenemos el valor maximo de id segun el id de cada producto obtenido mediante la funcin obtener_id(), y se almacena el diccionario con mayor valor de id
    id_aux = maximo_id["id"]    # Guardamos el valor de id del diccionario del producto obtenido
    id = id_aux + 1 # Sumamos 1 al id maximo para que no hayan ids repetidos
    
    #DESPUES REVISAR Y BORRAR COMENTARIOS MUERTOS COMO EL MODO = 'ALTA'
    #modo = "alta"   # Establecemos el modo de busqueda en alta
    nombre, marca = busqueda_producto_alta(productos)  # Llamamos a la funcion busqueda_producto() en modo alta, y guardamos el nombre y marca obtenidos
        
    precio = float(input("\tIngrese el precio (sin signos): "))
    while precio <= 0:
        precio = float(input("\tError. Ingrese el precio (sin signos): "))
        
    ubicacion = input("\tIngrese la ubicacion: ")
    
    stock = int(input("\tIngrese el stock: "))
    while stock < 1:
        stock = int(input("\tError. Ingrese el stock: "))
    
    print("\t¿Desea agregar una promocion? \n\t\t1.Si \n\t\t2.No")  # Mostramos menu promocion
    print()
    promo = int(input("\t\tOpcion: "))
    while promo < 1 or promo > 2:
        promo = int(input("\t\tError. Ingrese una opcion correcta: ")) 
        
    if promo == 1:  # Si se agrega promocion
        print("\tQue promocion desea agregar (ejemplos): \n\t\t1.NxM \n\t\t2.N'%' en la M unidad \n\t\t3.N'%' de descuento")    # Mostramos menu opciones de promocion
        print()
        promo_opcion = int(input("\t\tOpcion: "))
        while promo_opcion < 1 or promo_opcion > 3:
            promo_opcion = int(input("\t\tError. Ingrese una opcion correcta: ")) 
        # Guardado de promociones con formato segun opcion seleccionada
        if promo_opcion == 1:
            valor_1 = int(input("Ingrese el primer valor: "))
            while valor_1 < 1:
                valor_1 = int(input("Error. Ingrese el primer valor: "))
            valor_2 = int(input("Ingrese el segundo valor: "))
            while valor_2 < 1:
                valor_2 = int(input("Error. Ingrese el segundo valor: "))
            promocion = str(valor_1) + "x" + str(valor_2) 
        elif promo_opcion == 2:
            valor_1 = int(input("Ingrese el primer valor: "))
            while valor_1 < 1 or valor_1 > 99:
                valor_1 = int(input("Error. Ingrese el primer valor: "))
            valor_2 = int(input("Ingrese el segundo valor: "))
            while valor_2 < 1:
                valor_2 = int(input("Error. Ingrese el segundo valor: "))
            promocion = str(valor_1) + str(valor_2)
        else:
            valor_1 = int(input("Ingrese el valor: "))
            while valor_1 < 1 or valor_1 > 99:
                valor_1 = int(input("Error. Ingrese el valor: "))
            promocion = str(valor_1)     
    else:   # Promocion valdra 0
        promocion = "0"
    
    # Añadir producto
    productos.append({"id": id, "nombre": nombre, "marca": marca, "precio": precio, "ubicacion": ubicacion, "stock": stock, "promocion": promocion})    # Guardamos el nuevo producto junto con sus datos como un diccionario, mediante el append a la lista de diccionarios de productos
    
    productosJSON = json.dumps(productos, indent=4) # json.dumps() toma la lista de productos y lo convierte a una cadena en formato JSON, indent=4 le da formato al JSON resultante con una indentación de 4 espacios, para que sea más fácil de leer. Y por ultimo se almacena en productosJSON
    try:    # Manejo de excepciones (si cualquier linea dentro de try lanza error, pasa al except)
        archivo = open("productos.json", "w")   # Abrimos el archivo productos.json en modo escritura y guardamos el objeto del archivo en archivo
        archivo.write(productosJSON)    # Se guarda el contenido mediante write de la variable productosJSON (que tiene los productos en formato JSON) dentro del archivo
        archivo.close() # Cerramos el archivo leido
        print("Producto agregado!")
    except: # Si hubo alguna excepcion
        print("No se puede grabar el archivo productos")

def obtener_id(elemento):
    """
        Función para obtener el valor del campo "id"
        Es una función de apoyo para encontrar el ID más alto cuando agregamos un nuevo producto.
    """
    
    return elemento['id']

def baja_producto(productos):
    """
        Esta funcion elimina un producto de la lista según su ID.
        Si el ID no existe, te pide otro.
        Una vez eliminado, guarda los cambios en el archivo JSON.
    """
    
    mostrar_info_productos()    # Llamamos a la funcion mostrar_info_productos() para mostrar la info de todos los productos y poder ver cual dar de baja
    
    print()
    
    #modo = "baja"   # Establecemos el modo de busqueda en baja
    idProducto, encontrado = busqueda_producto_baja(productos) # Llamamos a la funcion busqueda_producto() en modo baja, y guardamos el id y el diccionario del producto encontrado

    if encontrado : # Si se encontro el producto
         productos_actualizados = [producto for producto in productos if producto['id'] != idProducto]  # Creamos una lista de diccionarios de productos por comprension, en donde todos los productos tengan id distinto al producto a eliminar
    
    productosJSON = json.dumps(productos_actualizados, indent=4)    # json.dumps() toma la lista de productos y lo convierte a una cadena en formato JSON, indent=4 le da formato al JSON resultante con una indentación de 4 espacios, para que sea más fácil de leer. Y por ultimo se almacena en productosJSON
    try:    # Manejo de excepciones (si cualquier linea dentro de try lanza error, pasa al except)
        archivo = open("productos.json", "w") # Abrimos el archivo productos.json en modo escritura y guardamos el objeto del archivo en archivo
        archivo.write(productosJSON)    # Se guarda el contenido mediante write de la variable productosJSON (que tiene los productos en formato JSON) dentro del archivo
        archivo.close() # Cerramos el archivo leido
        print("Producto eliminado con exito")
    except: # Si hubo alguna excepcion
        print("No se pudo eliminar el producto en el archivo productos") 

def modificar_producto(productos):
    """
        Esta funcion modifica un producto de la lista según su ID.
        Si el ID no existe, te pide otro.
        Una vez encontrado, se solicitan todos los campos que se quieran modificar, luego guarda los cambios en el archivo JSON.
    """
    
    mostrar_info_productos()

    print()
    
    #modo = "modificacion"   # Establecemos el modo de busqueda en modificacion
    idProducto, encontrado = busqueda_producto_modificacion(productos) # Llamamos a la funcion busqueda_producto() en modo modificacion, y guardamos el id y el diccionario del producto encontrado
    
    opcion = 0  # Se inicializa en 0 ya que la peticion y validacion se manejara dentro del while
    while opcion != 7 and (opcion >= 1 or opcion <= 7): # Validamos que la opcion este dentro del rango, el sistema se detiene cuando se ingresa la opcion 7 de finalizar
        opcion = int(input("\nIndique qué campo desea modificar: \n"    # Menu datos a modificar
                           "\t1. Nombre\n"
                           "\t2. Marca\n"
                           "\t3. Precio\n"
                           "\t4. Ubicación\n"
                           "\t5. Stock\n"
                           "\t6. Promoción\n"
                           "\t7. Finalizar (guardar y salir)\n"
                           "\tOpción: "))

        if opcion == 1:
            nombre = input("\tIngrese el nuevo nombre: ")
            encontrado['nombre'] = nombre   # Reemplazamos el valor de nombre en el diccionario del producto a modificar

        elif opcion == 2:
            marca = input("\tIngrese la nueva marca: ")
            encontrado['marca'] = marca # Reemplazamos el valor de marca en el diccionario del producto a modificar

        elif opcion == 3:
            precio = float(input("\tIngrese el nuevo precio (sin signos): "))
            while precio <= 0:
                precio = float(input("\tError. Ingrese un precio válido (sin signos): "))
            encontrado['precio'] = precio   # Reemplazamos el valor de precio en el diccionario del producto a modificar

        elif opcion == 4:
            ubicacion = input("\tIngrese la nueva ubicación: ")
            encontrado['ubicacion'] = ubicacion # Reemplazamos el valor de ubicacion en el diccionario del producto a modificar

        elif opcion == 5:
            stock = int(input("\tIngrese el nuevo stock: "))
            while stock < 1:
                stock = int(input("\tError. Ingrese un stock válido: "))
            encontrado['stock'] = stock # Reemplazamos el valor de stock en el diccionario del producto a modificar

        elif opcion == 6:
            print("\t¿Desea agregar una promoción? \n\t\t1. Sí \n\t\t2. No")
            promo = int(input("\t\tOpción: "))
            while promo < 1 or promo > 2:
                promo = int(input("\t\tError. Ingrese una opción correcta: ")) 
            
            promocion = "0" # Si no se desea promocion, valdra 0
            # Guardado de promociones con formato segun opcion seleccionada
            if promo == 1:
                print("\t¿Qué promoción desea agregar? (ejemplos): \n\t\t1. NxM \n\t\t2. N'%' en la M unidad \n\t\t3. N'%' descuento")
                promo_opcion = int(input("\t\tOpción: "))
                while promo_opcion < 1 or promo_opcion > 3:
                    promo_opcion = int(input("\t\tError. Ingrese una opción correcta: ")) 
                
                if promo_opcion == 1:
                    valor_1 = int(input("Ingrese el primer valor: "))
                    while valor_1 < 1:
                        valor_1 = int(input("Error. Ingrese el primer valor: "))
                    valor_2 = int(input("Ingrese el segundo valor: "))
                    while valor_2 < 1:
                        valor_2 = int(input("Error. Ingrese el segundo valor: "))
                    promocion = f"{valor_1}x{valor_2}"
                elif promo_opcion == 2:
                    valor_1 = int(input("Ingrese el porcentaje: "))
                    while valor_1 < 1 or valor_1 > 99:
                        valor_1 = int(input("Error. Ingrese el porcentaje: "))
                    valor_2 = int(input("Ingrese la unidad: "))
                    while valor_2 < 1:
                        valor_2 = int(input("Error. Ingrese el segundo valor: "))
                    promocion = str(valor_1) + str(valor_2)
                elif promo_opcion == 3:
                    valor_1 = int(input("Ingrese el porcentaje de descuento: "))
                    while valor_1 < 1 or valor_1 > 99:
                        valor_1 = int(input("Error. Ingrese el porcentaje de descuento: "))
                    promocion = str(valor_1)
            
            encontrado['promocion'] = promocion # Reemplazamos el valor de promocion en el diccionario del producto a modificar

        elif opcion == 7:   # Si la opcion es 7, es decir finalizar, se guardan los cambios en el archivo
            productosJSON = json.dumps(productos, indent=4) # json.dumps() toma la lista de productos y lo convierte a una cadena en formato JSON, indent=4 le da formato al JSON resultante con una indentación de 4 espacios, para que sea más fácil de leer. Y por ultimo se almacena en productosJSON
            try:    # Manejo de excepciones (si cualquier linea dentro de try lanza error, pasa al except)
                archivo = open("productos.json", "w")   # Abrimos el archivo productos.json en modo escritura y guardamos el objeto del archivo en archivo
                archivo.write(productosJSON)    # Se guarda el contenido mediante write de la variable productosJSON (que tiene los productos en formato JSON) dentro del archivo
                archivo.close() # Cerramos el archivo leido
                print("Producto modificado con éxito y archivo actualizado.")
            except: # Si hubo alguna excepcion
                print("No se pudo modificar el producto en el archivo productos.")
        else:   # Se ingreso una opcion incorrecta del menu
            print("Opcion incorrecta, vuelva a ingresar una valida.")

def mostrar_info_productos():
    """
        La diferencia con la funcion mostrar menu productos es que esta solo muestra la tabla de manera informativa, no permite realizar acciones como filtrar
    """
    
    print()
    productos = leer_archivo()  # Leemos y guardamos los productos
    
    # Obtener las claves (nombres de las columnas) desde el primer elemento del JSON, ya que es una lista de diccionarios
    columnas = list(productos[0].keys())    # Convertimos la claves en una lista mediante list() para poder usar los nombre como columnas
    
    # Calcular el ancho de cada columna (máximo entre el largo del nombre de la clave y los valores)
    anchuras = {columna: len(columna) for columna in columnas}  # Creamos un diccionario anchuras donde las claves son los nombres de las columnas y los valores son la longitud del nombre de la columna
    for fila in productos:  # Por cada producto (diccionario) de la lista de productos
        for columna in columnas:    # Por cada columna del producto
            anchuras[columna] = max(anchuras[columna], len(str(fila[columna]))) # Calcula el mayor valor entre el ancho actual de la columna y la longitud del valor de la columna en la fila actual. Se convierte el valor con str() para poder usar len(). El objetivo es que cada columna tenga el ancho suficiente para contener los valores mas largos
    
    # Imprimir la cabecera y separador
    cabecera = " | ".join([columna.ljust(anchuras[columna]) for columna in columnas])   # Mediante (" | ".join) se crea una cadena de texto donde los nombres de las columnas estan separados por "|". Luego (columna.ljust(anchuras[columna])) alinea los nombres de las columnas a la izquierda, asegurandose de cada columna tenga el ancho maximo calculado en el paso previo
    separador = "-+-".join(['-' * anchuras[columna] for columna in columnas])   # Mediante ("-+-".join([...])) se crea una cadena de texto donde cada columna esta separada por "-+-". Luego ('-' * anchuras[columna]) genera una linea de "-" cuyo largo coincide con el ancho de cada columna
    print(cabecera)     # Imprimimos la cabecera
    print(separador)    # Imprimimos el separador
    
    # Imprimir las filas de datos
    for fila in productos:  # Por cada producto (fila) en la lista de productos
        linea = " | ".join([str(fila[columna]).ljust(anchuras[columna]) for columna in columnas])   # Mediante (" | ".join([...])) se crea una cadena de texto donde los valores de las columnas están separados por " | ". Luego (str(fila[columna]).ljust(anchuras[columna])) convierte cada valor de la columna en una cadena de texto y lo alinea a la izquierda, utilizando el ancho calculado para la columna
        print(linea)    # Se imprime cada fila de productos, alineando los valores de cada columna

def menu_caja():
    """
        Esta funcion se encarga de todas las funciones de la caja, como las ventas y los importes. Una vez seleccionado e ingresado todo lo solicitado, actualiza el stock de los productos, 
        y agrega las ventas al JSON de ventas
    """
    
    print()
    
    ventas = leer_archivo_ventas()  # Leemos el archivo de ventas y almacenamos la lista de diccionarios de ventas obtenida
    
    #Día actual
    fecha = date.today()    # Conseguimos y guardamos la fecha de hoy mediante date.today()
    fecha = str(fecha)  # Transformamos la fecha a str para almacenarla luego en el json
    fecha_aux = date.today()    # Conseguimos y guardamos la fecha de hoy mediante date.today() en una variable auxiliar que usaremos para una tabla
    # En caso de querer simular ventas de otros dias podemos usar timedelta
    #nueva_fecha = fecha + timedelta(days=2) #Para agregar ventas con otras fechas
    
    print("Menu Caja: \n\t1. Ingresar Productos \n\t2. Volver") # Mostramos el menu de la caja
    print()
    opcion = int(input("Opcion: "))
    while opcion < 1 or opcion > 2:
        opcion = int(input("Error. Ingrese una opcion correcta: "))
        
    while opcion == 1:  # Mientras se quiera agregar productos
        productos = leer_archivo()  # Leemos el archivo de productos y almacenamos la lista de diccionarios de productos obtenida
        mostrar_info_productos()    # Mostramos la tabla informativa de los productos para poder visualizar y seleccionar los productos
        print()
        
        lista_productos_venta = []  # Creamos una lista vacia donde se almacenaran las ventas de los productos vendidos
        
        importe_total = 0   # Creamos una variable para ir almacenando los importes de venta de cada producto y calcular el importe total de la venta
        
        # Obtener el diccionario con el valor máximo de "id"
        maximo_id = max(ventas, key=obtener_id) # Obtenemos el valor maximo de id segun el id de cada venta obtenida mediante la funcin obtener_id(), y se almacena el diccionario con mayor valor de id
        id_aux = maximo_id["id"]    # Guardamos el valor de id del diccionario de la venta obtenida
        id = id_aux + 1 # Sumamos 1 al id maximo para que no hayan ids repetidos
        
        #modo = "caja"   # Establecemos el modo de busqueda en caja
        idProducto, encontrado = busqueda_producto_caja(productos) # Llamamos a la funcion busqueda_producto() en modo caja, y guardamos el id y el diccionario del producto encontrado
    
        cantidad = int(input("\t\tIngrese la cantidad de unidades a comprar: "))
        while cantidad > encontrado['stock']:   # Corroboramos que la cantidad de unidades compradas del producto no supere a las de stock disponible
            cantidad = int(input("\t\tError. Stock insuficiente, ingrese la cantidad de unidades a comprar: "))
            
        imp = obtener_importe(encontrado['precio'], encontrado['promocion'], cantidad)  # Llamamos a la funcion obtener_importe(), y mediante el precio, promocion y cantidad, del producto obtenemos su importe
        importe_total += imp    # Sumamos el importe total del producto al importe total de la venta
        
        producto_tupla = (id, encontrado['nombre'], encontrado['marca'], imp, cantidad, fecha)  # Creamos una tupla con los datos del producto y los datos necesarios de la venta
        lista_productos_venta.append(producto_tupla)    # Añadimos la tupla generado con la informacion de la venta a la lista de productos vendidos que sera usada luego para mostrar el resumen de la venta
            
        agregar_prod = True # Mediante este booleano permitimos que siempre entre al siguiente menu en donde se connsultara si desea agregar mas productos a la venta
        while agregar_prod: # Mientras se desee agregar productos
            ventas.append({"id": id, "nombre": encontrado['nombre'], "marca": encontrado['marca'], "importe": imp, "cantidad": cantidad, "fecha": fecha})   # Se añade mediante append, la venta del producto como diccionario a la lista de diccionarios de ventas
            
            # Agregacion de venta a archivo de ventas
            ventasJSON = json.dumps(ventas, indent=4)   # json.dumps() toma la lista de ventas y la convierte a una cadena en formato JSON, indent=4 le da formato al JSON resultante con una indentación de 4 espacios, para que sea más fácil de leer. Y por ultimo se almacena en ventasJSON
            
            try:    # Manejo de excepciones (si cualquier linea dentro de try lanza error, pasa al except)
                archivo = open("ventas.json", "w")  # Abrimos el archivo ventas.json en modo escritura y guardamos el objeto del archivo en archivo
                archivo.write(ventasJSON)   # Se guarda el contenido mediante write de la variable ventasJSON (que tiene las ventas en formato JSON) dentro del archivo
                archivo.close() # Cerramos el archivo leido
                print("Venta agregada!")
            except: # Si hubo alguna excepcion
                print("No se puede grabar el archivo ventas")
                
            # Se modifica el stock del producto vendido
            encontrado['stock'] = encontrado['stock'] - cantidad    # Se calcula el nuevo stock del producto vendido

            productosJSON = json.dumps(productos, indent=4) # json.dumps() toma la lista de productos y la convierte a una cadena en formato JSON, indent=4 le da formato al JSON resultante con una indentación de 4 espacios, para que sea más fácil de leer. Y por ultimo se almacena en productosJSON
            try:    # Manejo de excepciones (si cualquier linea dentro de try lanza error, pasa al except)
                archivo = open("productos.json", "w")   # Abrimos el archivo productos.json en modo escritura y guardamos el objeto del archivo en archivo
                archivo.write(productosJSON)    # Se guarda el contenido mediante write de la variable productosJSON (que tiene las ventas en formato JSON) dentro del archivo
                archivo.close() # Cerramos el archivo leido
                print("Stock producto modificado con éxito y archivo actualizado.")
            except: # Si hubo alguna excepcion
                print("No se pudo modificar el stock del producto en el archivo productos.")
                
            print()
            print("\t\t¿Desea agregar otro producto?: \n\t\t1. Si \n\t\t2. No") # Mostramos menu agregar productos
            opcion = int(input("Opcion: "))
            while opcion < 1 or opcion > 2:
                opcion = int(input("Error. Ingrese una opcion correcta: "))
            if opcion == 1: # Si se desea agregar otro, volvemos a realizar el procedimiento de busqueda y creacion de venta
                idProducto, encontrado = busqueda_producto_caja(productos) 
                # Obtener el diccionario con el valor máximo de "id"
                maximo_id = max(ventas, key=obtener_id) 
                id_aux = maximo_id["id"]    
                id = id_aux + 1 
    
                cantidad = int(input("\t\tIngrese la cantidad de unidades a comprar: "))
                while cantidad > encontrado['stock']:
                    cantidad = int(input("\t\tError. Stock insuficiente, ingrese la cantidad de unidades a comprar: "))
                    
                imp = obtener_importe(encontrado['precio'], encontrado['promocion'], cantidad)
                importe_total += imp
                
                producto_tupla = (id, encontrado['nombre'], encontrado['marca'], imp, cantidad, fecha)
                lista_productos_venta.append(producto_tupla)
            else:   # Si no se desea agregar mas productos, se mostrara el resumen de la venta
                print(f"Fecha: {formato_fecha(fecha_aux)}") # Mostramos la fecha de hoy, la cual sera la fecha que se guardara para la venta, y utilizamos la funcion formato_Fecha() para mostrarla de forma prolija
                
                # Títulos de las columnas
                columnas = ['Producto', 'Nombre', 'Marca', 'Importe', 'Cantidad']   # Creamos una lista de columnas, con el nombre de cada columna que tendra el resumen final
                
                # Mapeo de índices de las columnas (para acceder correctamente a las tuplas)
                indices = { # Generamos un diccionario con clave: nombre de la columna, y valor: indice de la columna en la tupla
                    'Producto': 0,
                    'Nombre': 1,
                    'Marca': 2,
                    'Importe': 3,
                    'Cantidad': 4
                }
                
                # Calcular el ancho de cada columna (máximo entre el largo del nombre de la clave y los valores)
                anchuras = {columna: len(columna) for columna in columnas}  # Creamos un diccionario anchuras donde las claves son los nombres de las columnas y los valores son la longitud del nombre de la columna
                for fila in lista_productos_venta:  # Por cada tupla en la lista de tuplas de ventas
                    for columna in columnas:    # Por cada columna de la tupla
                        anchuras[columna] = max(anchuras[columna], len(str(fila[indices[columna]])))    # Calcula el mayor valor entre el ancho actual de la columna y la longitud del valor de la columna en la fila actual. Se convierte el valor con str() para poder usar len(). El objetivo es que cada columna tenga el ancho suficiente para contener los valores mas largos
                        
                # Imprimir la cabecera
                cabecera = " | ".join([columna.ljust(anchuras[columna]) for columna in columnas])   # Mediante (" | ".join) se crea una cadena de texto donde los nombres de las columnas estan separados por "|". Luego (columna.ljust(anchuras[columna])) alinea los nombres de las columnas a la izquierda, asegurandose de cada columna tenga el ancho maximo calculado en el paso previo
                separador = "-+-".join(['-' * anchuras[columna] for columna in columnas])   # Mediante ("-+-".join([...])) se crea una cadena de texto donde cada columna esta separada por "-+-". Luego ('-' * anchuras[columna]) genera una linea de "-" cuyo largo coincide con el ancho de cada columna
                print(cabecera)     # Se imprime la cabecera
                print(separador)    # Se imprime el separador
                
                # Imprimir las filas de datos
                for fila in lista_productos_venta:  # Por cada venta (fila) en la lista de ventas
                    linea = " | ".join([str(fila[indices[columna]]).ljust(anchuras[columna]) for columna in columnas])  # Mediante (" | ".join([...])) se crea una cadena de texto donde los valores de las columnas están separados por " | ". Luego (str(fila[columna]).ljust(anchuras[columna])) convierte cada valor de la columna en una cadena de texto y lo alinea a la izquierda, utilizando el ancho calculado para la columna
                    print(linea)    # Se imprime cada fila de ventas, alineando los valores de cada columna
                    
                # Imprimir el total al final
                print(f"\n{'':>60} Importe Total: {importe_total:,.2f}")    # Utilizamos una cadena formateada para mostrar el importe total. Mediante ({'':>60}) añadimos una cadena vacia con un largo de 60 caracteres, para dejar ese espacio y el importe quede en la derecha. Luego con (:,.2f), la "," añade comas como separadores de miles, y el ".2f" formatea el numero como un decimal con 2 lugares despues del punto  
                
                print()
                print("\tSeleccione el metodo de pago: ")   # Mostramos el menu metodo de pago
                print("\t1. Efectivo \n\t2. Tarjeta")   # Mostramos opciones de pago
                opcion = int(input("Opcion: "))
                while opcion < 1 or opcion > 2:
                    opcion = int(input("Error. Ingrese una opcion correcta: "))
                
                if opcion == 1: #Si paga en efectivo, se debe calcular el cambio en caso sea necesario
                    pago = float(input("\tIngrese la cantidad con la que pagara el cliente: "))
                    while pago < importe_total: # Corroboramos que el cliente pague igual o mas del importe total de la venta
                        pago = float(input("\tError. Pago insuficiente. Ingrese la cantidad con la que pagara el cliente: "))
                    if pago > importe_total:    # Si el cliente pago mas del total, se le debe entregar vuelto
                        print(f"El vuelto es: ${pago - importe_total}") # Devolvemos un mensaje con el vuelto a entregar al cliente
                    else:   # Si el cliente pago justo
                        print("No es necesario entregar vuelto.")
                else:   # Si paga con tarjeta, no se le debe entregar cambio
                    print("No es necesario entregar vuelto.")
                agregar_prod = False    # Al finalizar la venta, se setea en False para terminar el bucle de la venta, ya que no se agregaran mas productos
                    
        print()
        print("Menu Caja: \n\t1. Ingresar Productos \n\t2. Volver") # Mostramos el menu de caja por si se quiere realizar otra venta
        print()
        opcion = int(input("Opcion: "))
        while opcion < 1 or opcion > 2:
            opcion = int(input("Error. Ingrese una opcion correcta: "))   
        if opcion == 2: # Selecciono volver
            return
    else:   # Selecciono volver
        return

def obtener_importe(importe, promocion, cantidad):
    """
        Esta funcion genera el importe total de un producto segun la cantidad de este, y el tipo de promocion que posea
    """
    
    # Caso 1: Promoción del tipo "MxN" (ejemplo: "2x3")
    if 'x' in promocion:    # Chequeamos si hay una "x" en el str promocion
        m, n = map(int, promocion.split('x'))   # Mediante (promocion.split('x')) dividimos la promcion en 2 partes separando por la "x", luego con (map(int, )) convertimos la lista con las 2 cadenas resultantes, en enteros. Y por ultimo, asignamos cada numero, uno a M y otro a N
        grupos = cantidad // n  # Calculamos cuantos grupos aplican a la promocion, por ejemplo si llevo 6, pago 4
        restantes = cantidad % n    # Calculamos cuantas unidades no entran en la promocion, por ejemplo si llevamos 7 unidades con 2x3, cantidad % n = 7 % 3 = 1, queda 1 unidad fuera de la promocion
        total = grupos * m * importe + restantes * importe  # Calculamos el total:
                                                            # grupos * m * importe: Calcula el costo de los grupos completos. Pagas m unidades por cada grupo, y hay grupos de estos, por lo que multiplicas grupos por m y por el precio unitario importe
                                                            # restantes * importe: Calcula el costo de las unidades restantes que no están cubiertas por la promoción
        return total    # Devolvemos el total
        '''
        Ejemplo:
        Si el precio por unidad es 100, compras 7 unidades, y la promoción es "2x3":
        grupos = 2, restantes = 1
        grupos * m * importe = 2 * 2 * 100 = 400 (pagas por 4 unidades en total en los grupos de la promoción)
        restantes * importe = 1 * 100 = 100 (pagas 1 unidad adicional fuera de la promoción)
        total = 400 + 100 = 500
        '''
    
    # Caso 2: Promoción del tipo "325" (ejemplo: "32% de descuento en la 5ta unidad")
    elif len(promocion) == 3 and promocion[-1].isdigit():   # Primero (len(promocion) == 3) verifica si la cadena de la promoción tiene exactamente 3 caracteres, luego (promocion[-1].isdigit()) verifica si el último carácter de la cadena es un número (esto indica que se refiere a la unidad en la que se aplica el descuento) 
        descuento = int(promocion[:2]) / 100  # Primero, (promocion[:2]) obtiene los primeros dos caracteres de la cadena, que representan el porcentaje de descuento, luego (int(promocion[:2])) convierte esa parte de la cadena en un entero, y por ultimo (/ 100) convierte el porcentaje en un valor decimal. Ejemplo: 32% -> 0.32
        unidad_descuento = int(promocion[-1])  # Primero, (promocion[-1]) obtiene el último carácter de la cadena, que representa la unidad en la que se aplicará el descuento, luego (int(promocion[-1])) convierte ese carácter en un entero. Ejemplo: 5ta unidad
        total = 0   # Creamos variable total para acumular el total de los productos
        for i in range(1, cantidad + 1):    # Recorre cada unidad que se va a comprar, desde la primera hasta la cantidad total (por eso empieza en 1, y se suma uno a la cantidad)
            if i == unidad_descuento:   # Si el número de la unidad actual (i) coincide con la unidad donde se aplica el descuento (por ejemplo, la 5ta unidad), se aplica el descuento
                total += importe * (1 - descuento)  # Suma el precio del producto con el descuento aplicado (por ejemplo, si el descuento es del 32%, el precio se multiplica por 0.68)
            else:   #  Para las otras unidades (que no tienen descuento), simplemente suma el precio completo al total
                total += importe    # Sumamos el precio al total
        return total    # Devolvemos el total
        '''
        Ejemplo:
        Si compras 7 unidades con una promoción "32% de descuento en la 5ta unidad" y el precio por unidad es 100:
        Las primeras 4 unidades se suman a precio completo: 100 + 100 + 100 + 100
        La 5ta unidad tiene un 32% de descuento, por lo que se suma 100 * (1 - 0.32) = 68
        Las unidades 6 y 7 se suman a precio completo: 100 + 100
        '''
    
    # Caso 3: Promoción del tipo "35" (ejemplo: "35% de descuento en todas las unidades)
    elif len(promocion) == 2 and promocion.isdigit():   # Primero (len(promocion) == 2) verifica si la cadena de la promoción tiene exactamente 2 caracteres, luego (promocion.isdigit()) verifica si la cadena contiene únicamente números (es decir, un valor como "35")
        descuento = int(promocion) / 100  # Primero (int(promocion)) convierte la cadena de promoción en un entero, luego (/ 100) convierte el porcentaje en un valor decimal. Ejemplo: 35% -> 0.35
        total = cantidad * importe * (1 - descuento)    # (cantidad * importe) calcula el precio total de todas las unidades antes de aplicar el descuento, y (1 - descuento) aplica el descuento
        return total    # Devolvemos el total
        '''
        Ejemplo:
        Si compras 5 unidades de un producto cuyo precio es 100, con un descuento del 35%:
        cantidad * importe = 5 * 100 = 500 (precio sin descuento)
        1 - descuento = 1 - 0.35 = 0.65 (solo pagas el 65% del precio original)
        total = 500 * 0.65 = 325 (precio total con el descuento aplicado)
        '''
    
    # Sin promoción
    else:
        return cantidad * importe   # Simplemente devolvemos (la cantidad de unidades compradas * el importe por unidad)
        '''
        Ejemplo:
        Si compras 5 unidades de un producto cuyo precio es 100, sin descuentos:
        cantidad * importe = 5 * 100 = 500
        total = 500
        '''

def formato_fecha(fecha):
    """
        Esta funcion simplemente formatea la fecha para que sea mas atractiva al mostrar en el recibo de la caja
    """
    
    meses = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")    # Se crea una tupla con cada mes del año
    dia = fecha.day # fecha.day extrae el dia de la fecha
    mes = meses[fecha.month - 1]    # fecha.month - 1: Extrae el número del mes y lo ajusta a la tupla meses (el índice de la tupla comienza en 0, por lo que se resta 1 al mes)
    año = fecha.year    # fecha.year extrae el año de la fecha
    messsage = "{} de {} del {}".format(dia, mes, año)  # Formateamos el mensaje de salida reemplazando con el dia, mes y año obtenidos. Por ejemplo, si la fecha es "2024-09-23", el mensaje generado sería: "23 de Septiembre del 2024"

    return messsage

def menu_salir():
    """
        Esta funcion solo muestra un banner con un mensaje de despedida al usuario mediante un print
    """

    banner = """
         _ _   _           _          _                           _ 
        (_) | | | __ _ ___| |_ __ _  | |   _   _  ___  __ _  ___ | |
        | | |_| |/ _` / __| __/ _` | | |  | | | |/ _ \/ _` |/ _ \| |
        | |  _  | (_| \__ \ || (_| | | |__| |_| |  __/ (_| | (_) |_|
        |_|_| |_|\__,_|___/\__\__,_| |_____\__,_|\___|\__, |\___/(_)
                                                      |___/         
    """
    print(banner)
    
# Funcion Principal
def main ():
    """
        Esta es la funcion principal, encargada de interactuar y movernos por el programa segun las opciones elegidas
    """
    
    opcion_menu_principal = menu_principal()     # Llamado a la funcion menu_principal() y almacenado de opcion
    
    if opcion_menu_principal == 1:  # Selecciono consultar productos
        menu_info_productos()   # Llamado a funcion menu_info_productos()
        main()  # Al finalizar volver a correr main() para mostrar el menu principal
    elif opcion_menu_principal == 2:
        menu_abm_productos()    # Llamado a funcion menu_abm_productos()
        main()  # Al finalizar volver a correr main() para mostrar el menu principal
    elif opcion_menu_principal == 3:
        menu_caja() # Llamado a funcion menu_caja()
        main()  # Al finalizar volver a correr main() para mostrar el menu principal
    elif opcion_menu_principal == 4:    # Funcion estadisticas en construccion
        print()
    else:   # Selecciono salir del programa
        menu_salir()    # Llamado a funcion menu_salir() para mostrar mensaje de salida
    
main()      #Llamado a la funcion principal