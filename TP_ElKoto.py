import json

'''
Anotaciones:

Promociones: 2x1 se guarda como texto "2x1", descuentos se guarda el % ej: 45, descuentos en x unidad se guarda ej: 25% en 2 unidad -> 252
Ademas las promociones son unicamente enteros. En caso de no tener promocion se indica con un 0.

JSON: Todo lo que se ingrese al JSON debe ingresarse sin tildes.
'''

#Funcion Menu Inicial
def menu_principal():
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
    try:
        archivo = open("TP_ElKoto_Algoritmos_I/productos.json", "r")
        lineas_productos = archivo.read()
        archivo.close()
    
        if len(lineas_productos) == 0:
            print("El archivo JSON está vacío o no contiene datos.")
            return
    
        productos = json.loads(lineas_productos)
        return productos
        
    except:
        print("No se puede abrir el archivo productos")

def menu_info_productos():
    print()
    productos = leer_archivo()
    
    # Obtener las claves (nombres de las columnas) desde el primer elemento del JSON
    columnas = list(productos[0].keys())
    
    # Calcular el ancho de cada columna (máximo entre el largo del nombre de la clave y los valores)
    anchuras = {columna: len(columna) for columna in columnas}
    for fila in productos:
        for columna in columnas:
            anchuras[columna] = max(anchuras[columna], len(str(fila[columna])))
    
    # Imprimir la cabecera
    cabecera = " | ".join([columna.ljust(anchuras[columna]) for columna in columnas])
    separador = "-+-".join(['-' * anchuras[columna] for columna in columnas])
    print(cabecera)
    print(separador)
    
    # Imprimir las filas de datos
    for fila in productos:
        linea = " | ".join([str(fila[columna]).ljust(anchuras[columna]) for columna in columnas])
        print(linea)
      
    print()  
    print("Menu Consulta Producto: \n\t1. Busqueda por Nombre \n\t2. Busqueda por Marca \n\t3. Busqueda por Promocion \n\t4. Volver")
    
    print()
    opcion = int(input("Opcion: "))
    while opcion < 1 or opcion > 4:
        opcion = int(input("Error. Ingrese una opcion correcta: "))
        
    while opcion >= 1 and opcion <= 3:
        if opcion == 1:
            columna_busqueda = "nombre"
            valor_busqueda = input("Ingrese el Nombre del Producto: ")
            print()
            busqueda_filtrada(productos, columna_busqueda, valor_busqueda)
        elif opcion == 2:
            columna_busqueda = "marca"
            valor_busqueda = input("Ingrese la Marca del Producto: ")
            print()
            busqueda_filtrada(productos, columna_busqueda, valor_busqueda)
        else:
            columna_busqueda = "promocion"
            valor_busqueda = input("Ingrese la Promocion del Producto: ")
            print()
            busqueda_filtrada(productos, columna_busqueda, valor_busqueda)
        
        print()    
        print("Menu Consulta Producto: \n\t1. Busqueda por Nombre \n\t2. Busqueda por Marca \n\t3. Busqueda por Promocion \n\t4. Volver")
        print()
        opcion = int(input("Opcion: "))
        while opcion < 1 or opcion > 4:
            opcion = int(input("Error. Ingrese una opcion correcta: "))     
    else:
        return
        
def busqueda_filtrada(productos, columna_busqueda, valor_busqueda):

    # Obtener las claves (nombres de las columnas) desde el primer elemento del JSON
    columnas = list(productos[0].keys())

    # Filtrar los datos según la columna y el valor de búsqueda
    datos_filtrados = [fila for fila in productos if valor_busqueda.lower() in str(fila.get(columna_busqueda, '')).lower()]

    # Verificar si hay resultados
    if len(datos_filtrados) == 0:
        print(f"No se encontraron resultados para '{valor_busqueda}' en la columna '{columna_busqueda}'.")
        return

    # Calcular el ancho de cada columna (máximo entre el largo del nombre de la clave y los valores)
    anchuras = {columna: len(columna) for columna in columnas}
    for fila in datos_filtrados:
        for columna in columnas:
            anchuras[columna] = max(anchuras[columna], len(str(fila[columna])))

    # Imprimir la cabecera
    cabecera = " | ".join([columna.ljust(anchuras[columna]) for columna in columnas])
    separador = "-+-".join(['-' * anchuras[columna] for columna in columnas])
    print(cabecera)
    print(separador)

    # Imprimir las filas de datos filtradas
    for fila in datos_filtrados:
        linea = " | ".join([str(fila[columna]).ljust(anchuras[columna]) for columna in columnas])
        print(linea)

def menu_abm_productos():
    print()
    print("Menu ABM Productos: \n\t1. Alta Producto \n\t2. Baja Producto \n\t3. Modificacion Producto \n\t4. Volver")
    
    print()
    opcion = int(input("Opcion: "))
    while opcion < 1 or opcion > 4:
        opcion = int(input("Error. Ingrese una opcion correcta: "))
        
    productos = leer_archivo()
        
    while opcion >= 1 and opcion <= 3:
        if opcion == 1:
            alta_producto(productos)
        elif opcion == 2:
            print("baja prod")
        else:
            print("mod prod")
            
        print("Menu ABM Productos: \n\t1. Alta Producto \n\t2. Baja Producto \n\t3. Modificacion Producto \n\t4. Volver")
        print()
        opcion = int(input("Opcion: "))
        while opcion < 1 or opcion > 4:
            opcion = int(input("Error. Ingrese una opcion correcta: "))     
    else:
        return
    
def alta_producto(productos):
    print("Datos del Producto: ")
    # Obtener el diccionario con el valor máximo de "id"
    maximo_id = max(productos, key=obtener_id)
    id_aux = maximo_id["id"]
    id = id_aux + 1
    
    nombre = input("\tIngrese el nombre: ")
    marca = input("\tIngrese la marca: ")
    # Variable para saber si encontramos el nombre
    encontrado = False

    # Recorrer la lista y verificar si algún diccionario tiene el nombre y marca buscado
    for diccionario in productos:
        if diccionario['nombre'].lower() == nombre.lower() and diccionario['marca'].lower() == marca.lower():
            encontrado = True
            break
        
    while encontrado:
        print("El producto ya existe, ingrese otro por favor: ")
        nombre = input("\tIngrese el nombre: ")
        marca = input("\tIngrese la marca: ")
        encontrado = False
        for diccionario in productos:
            if diccionario['nombre'].lower() == nombre.lower() and diccionario['marca'].lower() == marca.lower():
                encontrado = True
                break
        
    precio = float(input("\tIngrese el precio (sin signos): "))
    while precio <= 0:
        precio = float(input("\tError. Ingrese el precio (sin signos): "))
        
    ubicacion = input("\tIngrese la ubicacion: ")
    
    stock = int(input("\tIngrese el stock: "))
    while stock < 1:
        stock = int(input("\tError. Ingrese el stock: "))
    
    print("\t¿Desea agregar una promocion? \n\t\t1.Si \n\t\t2.No")
    print()
    promo = int(input("\t\tOpcion: "))
    while promo < 1 or promo > 2:
        promo = int(input("\t\tError. Ingrese una opcion correcta: ")) 
        
    if promo == 1:
        print("\tQue promocion desea agregar (ejemplos): \n\t\t1.NxM \n\t\t2.N'%' en la M unidad \n\t\t3.N'%'")
        print()
        promo_opcion = int(input("\t\tOpcion: "))
        while promo_opcion < 1 or promo_opcion > 3:
            promo_opcion = int(input("\t\tError. Ingrese una opcion correcta: ")) 
        if promo_opcion == 1:
            valor_1 = int(input("Ingrese el primer valor: "))
            while valor_1 < 1:
                valor_1 = int(input("Error. Ingrese el primer valor: "))
            valor_2 = int(input("Ingrese el segundo valor: "))
            while valor_2 < 1:
                valor_2 = int(input("Error. Ingrese el segundo valor: "))
            promocion = valor_1 + "x" + valor_2
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
    else:
        promocion = "0"
    
    productos.append({"id": id, "nombre": nombre, "marca": marca, "precio": precio, "ubicacion": ubicacion, "stock": stock, "promocion": promocion})
    productosJSON = json.dumps(productos, indent=4)
    try:
        archivo = open("TP_ElKoto_Algoritmos_I/productos.json", "w")
        archivo.write(productosJSON)
        archivo.close()
        print("Producto agregado!")
    except:
        print("No se puede grabar el archivo productos")
        
# Función para obtener el valor del campo "id"
def obtener_id(elemento):
    return elemento['id']

def menu_salir():
    banner = """
         _ _   _           _          _                           _ 
        (_) | | | __ _ ___| |_ __ _  | |   _   _  ___  __ _  ___ | |
        | | |_| |/ _` / __| __/ _` | | |  | | | |/ _ \/ _` |/ _ \| |
        | |  _  | (_| \__ \ || (_| | | |__| |_| |  __/ (_| | (_) |_|
        |_|_| |_|\__,_|___/\__\__,_| |_____\__,_|\___|\__, |\___/(_)
                                                      |___/         
    """
    print(banner)
    
#Funcion Principal
def main ():
    opcion_menu_principal = menu_principal()     #Llamado a la funcion menu inicial y almacenado de opcion
    
    if opcion_menu_principal == 1:
        menu_info_productos()
        main()
    elif opcion_menu_principal == 2:
        menu_abm_productos()
        main()
    elif opcion_menu_principal == 3:
        print()
    elif opcion_menu_principal == 4:
        print()
    else:
        menu_salir()
    
main()      #Llamado a la funcion principal