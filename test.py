import unittest
from unittest.mock import patch
from main import obtener_suposicion_ordenador, obtener_suposicion_jugador, comparar_suposiciones, jugar, main
class TestGuessTheNumber(unittest.TestCase):

    def test_obtener_suposicion_ordenador(self):
        random_number =  obtener_suposicion_ordenador ()

        # Verifica que el número sea entre 1 y 100
        self.assertGreaterEqual(random_number, 1)
        self.assertLessEqual(random_number, 100)

    @patch('builtins.input', side_effect=['50', '60', '70'])
    def test_player_guesses_correctly_in_third_attempt(self, mock_input):
        """
        Test para la función jugar, que verifica que la función termine correctamente cuando el jugador adivina el número en su tercer intento.
        """
        with patch('main.obtener_suposicion_ordenador', return_value=50):
            with patch('main.comparar_suposiciones', side_effect=[False, False, True]):
                jugar()

    @patch('builtins.input', side_effect=['-1', '101', '50'])
    def test_get_user_guess_invalid_input(self, mock_input):
        """
        Test para la función obtener_suposicion_jugador, que verifica que la función maneje correctamente 
        la entrada del usuario cuando se ingresan números negativos o números mayores que 100.
        """
        self.assertEqual(obtener_suposicion_jugador(), 50)  

    @patch('builtins.input', side_effect=['40'])
    def test_get_user_guess_valid_input(self, mock_input):
        """Test para la función GET USER GUESS, que verifica que el número ingresado esté en el rango del valor del juego"""
        self.assertEqual(obtener_suposicion_jugador(), 40)  

    def test_comparar_suposiciones(self):
        self.assertTrue(comparar_suposiciones(50, 50))
        self.assertFalse(comparar_suposiciones(50, 40))
        self.assertFalse(comparar_suposiciones(50, 60))
    


    



if __name__ == '__main__':
    unittest.main()
