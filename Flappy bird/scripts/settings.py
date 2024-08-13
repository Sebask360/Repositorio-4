import pygame

# Dimensiones de la pantalla
ANCHO = 1016
ALTO = 536

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

#rfedimensionar Ave
ANCHO_AVE = 40
ALTO_AVE = 40

# Velocidad y física del ave
GRAVEDAD = 0.25
SALTO = -4

# Tubos
TUBO_VELOCIDAD = 2
TUBO_INTERVALO = 150
TUBO_ESPACIO = 150
ALTURA_TUBO_MIN = 50
ALTURA_TUBO_MAX = ALTO - TUBO_ESPACIO - 50

# Fuente
FUENTE = pygame.font.SysFont('Arial', 30)