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
    mostrar_top_marcas
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

def test_busqueda_producto_alta(monkeypatch):
    inputs = iter(["Producto 1", "Marca 1"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    productos = [{"nombre": "Producto 2", "marca": "Marca 2"}]
    nombre, marca = busqueda_producto_alta(productos)
    assert nombre == "Producto 1"
    assert marca == "Marca 1"

def test_mostrar_top_promociones(capfd):
    ventas = [
        {"id": 1, "promocion": "2x1", "cantidad": 5},
        {"id": 2, "promocion": "30", "cantidad": 3},
        {"id": 3, "promocion": "2x1", "cantidad": 7},
        {"id": 4, "promocion": "10", "cantidad": 2},
    ]
    mostrar_top_promociones(ventas)
    captured = capfd.readouterr()
    assert "2x1" in captured.out
    assert "30" in captured.out
    assert "10" in captured.out

def test_mostrar_recaudacion_total_dia_mes(capfd):
    ventas = [
        {"id": 1, "importe": 100.0},
        {"id": 2, "importe": 200.5},
        {"id": 3, "importe": 50.0},
    ]
    mostrar_recaudacion_total_dia_mes(ventas)
    captured = capfd.readouterr()
    assert "350.5" in captured.out  # Verifica si la suma total es correcta

def test_mostrar_total_productos_vendidos(capfd):
    ventas = [
        {"id": 1, "cantidad": 5},
        {"id": 2, "cantidad": 3},
        {"id": 3, "cantidad": 7},
    ]
    mostrar_total_productos_vendidos(ventas)
    captured = capfd.readouterr()
    assert "15" in captured.out  # Verifica si el total de productos vendidos es correcto

def test_mostrar_top_marcas(capfd):
    ventas = [
        {"id": 1, "marca": "Marca A", "cantidad": 5},
        {"id": 2, "marca": "Marca B", "cantidad": 3},
        {"id": 3, "marca": "Marca A", "cantidad": 7},
        {"id": 4, "marca": "Marca C", "cantidad": 2},
        {"id": 5, "marca": "Marca B", "cantidad": 4},
    ]
    mostrar_top_marcas(ventas)
    captured = capfd.readouterr()
    assert "Marca A" in captured.out
    assert "Marca B" in captured.out
    assert "Marca C" in captured.out
