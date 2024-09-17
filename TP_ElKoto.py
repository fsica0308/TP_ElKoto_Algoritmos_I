import json

'''
Anotaciones:

Promociones: 2x1 se guarda como texto "2x1", descuentos se guarda el % ej: 45, descuentos en x unidad se guarda ej: 25% en 2 unidad -> 252
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
    archivo = open("TP_ElKoto_Algoritmos_I/productos.json", "r")
    lineas_productos = archivo.read()
    archivo.close()
    
    if len(lineas_productos) == 0:
        print("El archivo JSON está vacío o no contiene datos.")
        return
    
    productos = json.loads(lineas_productos)
    
    return productos

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
        
    while opcion >= 1 and opcion <= 3:
        if opcion == 1:
            print("alta prod")
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