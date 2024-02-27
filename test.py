import unittest
from main import obtener_suposicion_jugador, obtener_suposicion_ordenador, comparar_suposiciones

class TestJuego(unittest.TestCase):

    def test_obtener_suposicion_jugador(self):
        self.assertEqual(obtener_suposicion_jugador(), 5)

    def test_obtener_suposicion_ordenador(self):
        suposicion = obtener_suposicion_ordenador()
        self.assertIsInstance(suposicion, int)
        self.assertTrue(1 <= suposicion <= 100)

    def test_comparar_suposiciones(self):
        self.assertTrue(comparar_suposiciones(50, 50))
        self.assertFalse(comparar_suposiciones(50, 40))
        self.assertFalse(comparar_suposiciones(50, 60))

    

if __name__ == '__main__':
    unittest.main()
