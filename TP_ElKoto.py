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

def menu_abm_productos():
    print()
    print("Menu ABM Productos: \n\t1. Alta Producto \n\t2. Baja Producto \n\t3. Modificacion Producto \n\t4. Salir")
    
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
            
        print("Menu ABM Productos: \n\t1. Alta Producto \n\t2. Baja Producto \n\t3. Modificacion Producto \n\t4. Salir")
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
        print()
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