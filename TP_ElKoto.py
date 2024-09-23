import json

'''
Anotaciones:

Promociones: 2x1 se guarda como texto "2x1", descuentos se guarda el % ej: 45, descuentos en x unidad se guarda ej: 25% en 2 unidad -> 252
Ademas las promociones son unicamente enteros. En caso de no tener promocion se indica con un 0.

JSON: Todo lo que se ingrese al JSON debe ingresarse sin tildes.

Agregar comentarios de todo el codigo y agregar descripciones a las funciones con: """descripcion"""
'''

#Funcion Menu Inicial, muestra un banner de bienvenida mediante un print, luego le da la opcion al usuario 
# de seleccionar entre las opciones que cuenta el menu, valida que la opcion elegida este entre las opciones dadas
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

# Esta función abre el archivo 'productos.json' y carga su contenido.
# Si el archivo está vacío, muestra un mensaje indicando que no hay datos.
# Si todo sale bien, devuelve la información de los productos como un diccionario.
# En caso de que algo falle, muestra un mensaje de error.
def leer_archivo():
    try:
        archivo = open("productos.json", "r")
        lineas_productos = archivo.read()
        archivo.close()
    
        if len(lineas_productos) == 0:
            print("El archivo JSON está vacío o no contiene datos.")
            return
    
        productos = json.loads(lineas_productos)
        return productos
        
    except:
        print("No se puede abrir el archivo productos")


# Esta funcion uestra toda la información de los productos en formato de tabla.
# Además, permite buscar productos por nombre, marca o promoción.
# Luego de cada búsqueda, vuelve a mostrar el menú para hacer más consultas.
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
        


# Estan funcion filtra los productos según la columna y el valor que elijas (nombre, marca o promoción).
# Si no encuentra nada, te avisa. Si encuentra, te muestra los resultados en una tabla.       
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


 # Esta funcion muestra un menú donde puedes agregar, eliminar o modificar productos.
 # Te pide elegir una opción y ejecuta la función correspondiente (alta, baja o modificación).
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
            baja_producto(productos)
        else:
            modificar_producto(productos)
            
        print("Menu ABM Productos: \n\t1. Alta Producto \n\t2. Baja Producto \n\t3. Modificacion Producto \n\t4. Volver")
        print()
        opcion = int(input("Opcion: "))
        while opcion < 1 or opcion > 4:
            opcion = int(input("Error. Ingrese una opcion correcta: "))     
    else:
        return


# Esta funcion agrega un nuevo producto pidiendo los datos como nombre, marca, precio, ubicación y stock.
# Además, te da la opción de agregar una promoción al producto.
# Guarda el producto nuevo en el archivo JSON.
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
        print("\tQue promocion desea agregar (ejemplos): \n\t\t1.NxM \n\t\t2.N'%' en la M unidad \n\t\t3.N'%' de descuento")
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
            promocion = str(valor_1) + "x" + str(valor_2) #agregue parse a str pq sino rompia
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
            promocion = str(valor_1)   #agrego, faltaba asignar a variable promocion    
    else:
        promocion = "0"
    
    #uso .append para añadir el nuevo producto 
    productos.append({"id": id, "nombre": nombre, "marca": marca, "precio": precio, "ubicacion": ubicacion, "stock": stock, "promocion": promocion})
    
    #json.dumps(): Toma la lista de productos y lo convierte a una cadena en formato JSON.
    #indent=4: Le da formato al JSON resultante con una indentación de 4 espacios, para que sea más fácil de leer.
    productosJSON = json.dumps(productos, indent=4)
    try:
        #Abro el archivo a editar con open(), 
        #luego con archivo.write(productosJSON) guardo el contenido de la variable productosJSON 
        # (que tiene los productos en formato JSON) dentro del archivo. 
        # Por ultimo cierro el archivo con archivo.close()
        archivo = open("productos.json", "w") #open("TP_ElKoto_Algoritmos_I/productos.json", "w")
        archivo.write(productosJSON)
        archivo.close()
        print("Producto agregado!")
    except:
        print("No se puede grabar el archivo productos")

# Función para obtener el valor del campo "id"
# Es una función de apoyo para encontrar el ID más alto cuando agregamos un nuevo producto.
def obtener_id(elemento):
    return elemento['id']


# Esta funcion elimina un producto de la lista según su ID.
# Si el ID no existe, te pide otro.
# Una vez eliminado, guarda los cambios en el archivo JSON.
def baja_producto(productos):
    mostrar_info_productos()
    
    print()
    idProducto = int(input("\tIngrese el id del producto que desea eliminar: "))
    encontrado = False

    # Recorrer la lista y verificar si algún diccionario tiene el id del producto que se requiere eliminar
    for diccionario in productos:
        if diccionario['id'] == idProducto :
            encontrado = True
            #break   ->  es necesario ?? en este caso no vamos a tener tantos articulos como para que la 
            # busequeda se relentice, no recuerdo si este profe comento algo sobre si el break es una mala 
            # practica o solo fue el profe anterior     
        
    while not encontrado:
        print(f"El producto con id {idProducto} no existe, ingrese otro por favor: ")
        idProducto = int(input("\tIngrese el id del producto que desea eliminar: "))
        encontrado = False
        for diccionario in productos:
            if diccionario['id'] == idProducto :
                encontrado = True
                #break   ->  es necesario ?? en este caso no vamos a tener tantos articulos como para que la 
                # busequeda se relentice, no recuerdo si este profe comento algo sobre si el break es una mala 
                # practica o solo fue el profe anterior

    #si el producto existe en el listado, se guarda en una variable todos los items del listado donde el ID 
    #sea distinto al ID que deseamos eliminar, para luego reescribir el json sin este producto    
    if encontrado :
         productos_actualizados = [producto for producto in productos if producto['id'] != idProducto]
    
    #json.dumps(): Toma la lista de productos y lo convierte a una cadena en formato JSON.
    #indent=4: Le da formato al JSON resultante con una indentación de 4 espacios, para que sea más fácil de leer.
    productosJSON = json.dumps(productos_actualizados, indent=4)
    try:
        #Abro el archivo a editar con open(), 
        #luego con archivo.write(productosJSON) guardo el contenido de la variable productosJSON 
        # (que tiene los productos en formato JSON) dentro del archivo. 
        # Por ultimo cierro el archivo con archivo.close()
        archivo = open("productos.json", "w") #open("TP_ElKoto_Algoritmos_I/productos.json", "w") NO ME LEIA EL ARCHIVO SI PONIA LA RUTA CON LA CARPETA INCLUIDA
        archivo.write(productosJSON)
        archivo.close()
        print("Producto eliminado con exito")
    except:
        print("No se pudo eliminar el producto en el archivo productos") 

# Funcion de baja de articulos
def modificar_producto(productos):
    mostrar_info_productos()

    print()
    idProducto = int(input("\tIngrese el id del producto que desea modificar: "))
    #en este caso encontrado no va a ser bool porque quiero que guarde los datos del json que se quiere modificar
    encontrado = None

    # Recorrer la lista y verificar si algún diccionario tiene el id del producto que se requiere eliminar
    for diccionario in productos:
        if diccionario['id'] == idProducto :
            encontrado = diccionario
            
        
    while encontrado is None:
        print(f"El producto con id {idProducto} no existe, ingrese otro por favor: ")
        idProducto = int(input("\tIngrese el id del producto que desea modificar: "))
        encontrado = None
        for diccionario in productos:
            if diccionario['id'] == idProducto :
                encontrado = diccionario
        
    
    #Inicializo en 0 porque la peticion y validacion la manejo dentro del while
    opcion = 0
    #validamos que la opcion este dentro del rango, el sistema se detiene cuando se ingresa la opcion 7 de finalizar
    while opcion != 7 and (opcion >= 1 or opcion <= 7):  
        #le consulto que datos desea modificar
        opcion = int(input("\nIndique qué campo desea modificar: \n"
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
            encontrado['nombre'] = nombre

        elif opcion == 2:
            marca = input("\tIngrese la nueva marca: ")
            encontrado['marca'] = marca

        elif opcion == 3:
            precio = float(input("\tIngrese el nuevo precio (sin signos): "))
            while precio <= 0:
                precio = float(input("\tError. Ingrese un precio válido (sin signos): "))
            encontrado['precio'] = precio

        elif opcion == 4:
            ubicacion = input("\tIngrese la nueva ubicación: ")
            encontrado['ubicacion'] = ubicacion

        elif opcion == 5:
            stock = int(input("\tIngrese el nuevo stock: "))
            while stock < 1:
                stock = int(input("\tError. Ingrese un stock válido: "))
            encontrado['stock'] = stock

        elif opcion == 6:
            print("\t¿Desea agregar una promoción? \n\t\t1. Sí \n\t\t2. No")
            promo = int(input("\t\tOpción: "))
            while promo < 1 or promo > 2:
                promo = int(input("\t\tError. Ingrese una opción correcta: ")) 
            
            promocion = "0"
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
                    promocion = str(valor_1) + str(valor_2) # promocion = f"{valor_1}% en la {valor_2} unidad"
                elif promo_opcion == 3:
                    valor_1 = int(input("Ingrese el porcentaje de descuento: "))
                    while valor_1 < 1 or valor_1 > 99:
                        valor_1 = int(input("Error. Ingrese el porcentaje de descuento: "))
                    promocion = str(valor_1) # promocion = f"{valor_1}% descuento"
            
            encontrado['promocion'] = promocion

        elif opcion == 7:
            #json.dumps(): Toma la lista de productos y lo convierte a una cadena en formato JSON.
            #indent=4: Le da formato al JSON resultante con una indentación de 4 espacios, para que sea más fácil de leer.
            productosJSON = json.dumps(productos, indent=4)
            try:
                #Abro el archivo a editar con open(), 
                #luego con archivo.write(productosJSON) guardo el contenido de la variable productosJSON 
                # (que tiene los productos en formato JSON) dentro del archivo. 
                # Por ultimo cierro el archivo con archivo.close()
                archivo = open("productos.json", "w") #open("TP_ElKoto_Algoritmos_I/productos.json", "w") NO ME LEIA EL ARCHIVO SI PONIA LA RUTA CON LA CARPETA INCLUIDA
                archivo.write(productosJSON)
                archivo.close()
                print("Producto modificado con éxito y archivo actualizado.")
            except:
                print("No se pudo modificar el producto en el archivo productos.")
            # Si la opcion es 7, es decir finalizar, guardo los cambios en el archivo

        else:
            print("Opcion incorrecta, vuelva a ingresar una valida.")

# La diferencia con la funcion mostrar menu productos es que esta solo muestra la tabla de manera informativa, 
# no permite realizar acciones como filtrar
def mostrar_info_productos():
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

def funciones_caja():
    mostrar_info_productos()
    print()

#Esta funcion solo muestra un banner con un mensaje de despedida al usuario mediante un print
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