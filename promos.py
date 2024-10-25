import json

# Conjunto para almacenar promociones únicas
promociones = set()

# Función para agregar promociones
def agregar_promocion(promocion):
    # Añade la promoción al conjunto, evitando duplicados
    promociones.add(promocion)

# Ejemplo de promociones
agregar_promocion("2x1")
agregar_promocion("45")  # Descuento del 45%
agregar_promocion("252")  # Descuento del 25% en la 2ª unidad
agregar_promocion("2x1")  # Intento de duplicado

# Guardar el conjunto como lista en JSON
with open("promos.json", "w") as archivo:
    json.dump(list(promociones), archivo)