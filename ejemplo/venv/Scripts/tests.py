

from Scripts.main import obtener_suposicion_ordenador


def test_obtener_suposicion_ordenador():
    # Verifica que el número generado está dentro del rango permitido
    numero_aleatorio = obtener_suposicion_ordenador()
    assert 1 <= numero_aleatorio <= 100