# Import a library of functions called 'pygame'
import pygame
from main_functions import *

# Initialize the game engine
pygame.init()

# Nueva interpretación del tamaño de página.
size = [1300, 600]
ancho = int(input("Ancho de la pantalla: "))
alto = int(input("Alto de la pantalla: "))
size[0] = ancho
size[1] = alto
main2 (size)