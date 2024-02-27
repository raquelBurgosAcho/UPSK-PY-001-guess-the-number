# Importe el módulo random para generar números aleatorios
import random

# función que solicita al usuario que ingrese un número y lo devuelve como un entero (int)
def obtener_suposicion_jugador():
    """Obtiene la suposición del jugador."""
    return int(input("¿Elige un número? "))

# función que genera aleatoriamente un número entre 1 y 100 y lo devuelve.
def obtener_suposicion_ordenador():
    """Obtiene la suposición del ordenador."""
    return random.randint(1, 100)

# función que compara la suposición con el número aleatorio y proporciona retroalimentación al usuario sobre si la suposición es demasiado alta, demasiado baja 
def comparar_suposiciones(numero_aleatorio, suposicion):
    """Compara la suposición con el número aleatorio."""
    if suposicion == numero_aleatorio:
        print("¡Felicidades! ¡Has adivinado el número secreto!")
        return True
    elif suposicion < numero_aleatorio:
        print("Muy bajo. Intenta de nuevo.")
        return False
    else:
        print("Muy alto. Intenta de nuevo.")
        return False

def jugar():
    """Función principal para jugar el juego."""
    numero_aleatorio = random.randint(1, 100)
    print("El número aleatorio generado es:", numero_aleatorio)

# inicia dos listas vacías suposiciones_jugador y suposiciones_ordenador para almacenar las suposiciones de ambos    jugadores.
    suposiciones_jugador = []
    suposiciones_ordenador = []

    while True:
        intento_ordenador = obtener_suposicion_ordenador()
        suposiciones_ordenador.append(intento_ordenador)
        print("El ordenador elige:", intento_ordenador)

        if comparar_suposiciones(numero_aleatorio, intento_ordenador):
            break

        intento_jugador = obtener_suposicion_jugador()
        suposiciones_jugador.append(intento_jugador)

        if comparar_suposiciones(numero_aleatorio, intento_jugador):
            break

    print("Todas las suposiciones de la jugadora:", suposiciones_jugador)

while True:
    jugar()
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (si/No)")
    if jugar_de_nuevo.lower() != "si":
        break
