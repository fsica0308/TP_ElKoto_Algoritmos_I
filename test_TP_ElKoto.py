# test_tp_elkoto.py
import pytest
from TP_ElKoto import (
    limpiar_espacios,
    obtener_id,
    obtener_importe,
    formato_fecha,
    busqueda_producto_alta,
    mostrar_top_promociones,
    mostrar_recaudacion_total_dia_mes,
    mostrar_total_productos_vendidos,
    mostrar_top_marcas, 
    busqueda_filtrada
)

def test_limpiar_espacios():
    assert limpiar_espacios("  producto  ") == "producto"
    assert limpiar_espacios("  ejemplo") == "ejemplo"
    assert limpiar_espacios("test  ") == "test"
    assert limpiar_espacios("") == ""
    assert limpiar_espacios("   ") == ""  # Cadena vacía después de limpiar espacios

def test_obtener_id():
    elemento = {"id": 5}
    assert obtener_id(elemento) == 5
    elemento = {"id": 123}
    assert obtener_id(elemento) == 123

def test_obtener_importe():
    assert obtener_importe(100, "0", 5) == 500  # Sin promoción
    assert obtener_importe(100, "2x1", 7) == 400  # "2x1" promoción
    assert obtener_importe(100, "254", 5) == 418  # "25% en la 4ta unidad"
    assert obtener_importe(100, "35", 5) == 325  # "35% en todas"

def test_formato_fecha():
    from datetime import date
    fecha = date(2024, 9, 23)
    assert formato_fecha(fecha) == "23 de Septiembre del 2024"

def test_busqueda_filtrada():
    productos = [
        {"nombre": "Producto 1", "marca": "Marca A", "promocion": "2x1"},
        {"nombre": "Producto 2", "marca": "Marca B", "promocion": "30%"},
        {"nombre": "Producto 3", "marca": "Marca A", "promocion": "2x1"},
    ]
    columna_busqueda = "marca"
    valor_busqueda = "Marca A"
    
    resultado = busqueda_filtrada(productos, columna_busqueda, valor_busqueda)
    assert len(resultado) == 2
    assert resultado[0]["nombre"] == "Producto 1"
    assert resultado[1]["nombre"] == "Producto 3"


def test_mostrar_top_promociones():
    ventas = [
        {"id": 1, "promocion": "2x1", "cantidad": 5},
        {"id": 2, "promocion": "30", "cantidad": 3},
        {"id": 3, "promocion": "2x1", "cantidad": 7},
        {"id": 4, "promocion": "10", "cantidad": 2},
    ]
    resultado = mostrar_top_promociones(ventas)
    assert "2x1" in resultado
    assert "30" in resultado
    assert "10" in resultado


def test_mostrar_recaudacion_total_dia_mes():
    ventas = [
        {"id": 1, "importe": 100.0},
        {"id": 2, "importe": 200.5},
        {"id": 3, "importe": 50.0},
    ]
    total_recaudado = mostrar_recaudacion_total_dia_mes(ventas)
    assert total_recaudado == 350.5  #chequeo si el total recaudado es 350.5


def test_mostrar_total_productos_vendidos():
    ventas = [
        {"id": 1, "cantidad": 5},
        {"id": 2, "cantidad": 3},
        {"id": 3, "cantidad": 7},
    ]
    total_productos = mostrar_total_productos_vendidos(ventas)
    assert total_productos == 15  # Chequeo si el total de productos vendidos es 15

def test_mostrar_top_marcas():
    ventas = [
        {"id": 1, "marca": "Marca A", "cantidad": 5},
        {"id": 2, "marca": "Marca B", "cantidad": 3},
        {"id": 3, "marca": "Marca A", "cantidad": 7},
        {"id": 4, "marca": "Marca C", "cantidad": 2},
        {"id": 5, "marca": "Marca B", "cantidad": 4},
    ]
    top_marcas = mostrar_top_marcas(ventas)
    assert "Marca A" in top_marcas
    assert "Marca B" in top_marcas
    assert "Marca C" in top_marcas
    assert "Marca D" not in top_marcas

#tengo errores con pytest. no puedo realizar las pruebas en mi computadora.