import unittest
from unittest.mock import patch
from main import obtener_suposicion_ordenador, obtener_suposicion_jugador
class TestGuessTheNumber(unittest.TestCase):

    def test_obtener_suposicion_ordenador(self):
        random_number =  obtener_suposicion_ordenador ()

        # Verifica que el número sea entre 1 y 100
        self.assertGreaterEqual(random_number, 1)
        self.assertLessEqual(random_number, 100)

    @patch('builtins.input', side_effect=['40'])
    def test_get_user_guess_valid_input(self, mock_input):
        """Test para la función GET USER GUESS, que verifica que el número ingresado esté en el rango del valor del juego"""
        self.assertEqual(obtener_suposicion_jugador(), 40)    


if __name__ == '__main__':
    unittest.main()
