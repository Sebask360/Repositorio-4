import pygame
import random

# Inicializar Pygame
pygame.init()

#Importa settings
from settings import *

#Configuracion de la fuente
FUENTE = pygame.font.SysFont('Arial',30)

#Configuracion de la pantalla
pantalla = pygame.display.set_mode([ANCHO, ALTO])
pygame.display.set_caption('Flappy Bird')

# Reloj
reloj = pygame.time.Clock()

# Cargar imágenes
fondo = pygame.image.load('C:/Users/sebas/Documents/Programacion/Repositorio-4/Flappy bird/assets/images/background.png')
ave_original = pygame.image.load('C:/Users/sebas/Documents/Programacion/Repositorio-4/Flappy bird/assets/images/bird.png')
ave = pygame.transform.scale(ave_original, (ANCHO_AVE, ALTO_AVE)) 
altura_tubo = 150 
tubo_arriba = pygame.Surface((50, altura_tubo))
tubo_arriba.fill((0, 255, 0))  # Color verde para el tubo
tubo_abajo = pygame.transform.flip(tubo_arriba, False, True)


# Variables
ave_x = 50
ave_y = 200
ave_velocidad = 0
tubos = []
puntuacion = 0

# Función para generar tubos
def generar_tubos():
    altura = random.randint(ALTURA_TUBO_MIN, ALTURA_TUBO_MAX)
    tubos.append({'x': ANCHO, 'y': altura})

# Bucle principal
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ave_velocidad = SALTO

    # Mover el ave
    ave_velocidad += GRAVEDAD
    ave_y += ave_velocidad

    # Generar tubos
    if len(tubos) == 0 or tubos[-1]['x'] < ANCHO - TUBO_INTERVALO:
        generar_tubos()

    # Mover tubos
    for tubo in tubos:
        tubo['x'] -= TUBO_VELOCIDAD

    # Eliminar tubos fuera de pantalla
    tubos = [tubo for tubo in tubos if tubo['x'] > -50]

    # Rectángulos para el ave y los tubos
    ave_rect = pygame.Rect(ave_x, ave_y, ave.get_width(), ave.get_height())

    for tubo in tubos:
        tubo_rect_arriba = pygame.Rect(tubo['x'], tubo['y'] - tubo_arriba.get_height(), tubo_arriba.get_width(), tubo_arriba.get_height())
        tubo_rect_abajo = pygame.Rect(tubo['x'], tubo['y'] + TUBO_ESPACIO, tubo_abajo.get_width(), tubo_abajo.get_height())

        # Colisiones con los tubos
        if ave_rect.colliderect(tubo_rect_arriba) or ave_rect.colliderect(tubo_rect_abajo):
            game_over = True
            break

        # Incrementar la puntuación cuando el ave pasa un tubo
        if tubo['x'] + tubo_arriba.get_width() == ave_x:
            puntuacion += 1

    # Dibujar elementos
    pantalla.fill(BLANCO)
    pantalla.blit(fondo, (0, 0))
    pantalla.blit(ave, (ave_x, ave_y))
    for tubo in tubos:
        pantalla.blit(tubo_arriba, (tubo['x'], tubo['y'] - tubo_arriba.get_height()))
        pantalla.blit(tubo_abajo, (tubo['x'], tubo['y'] + TUBO_ESPACIO))

    puntuacion_texto = FUENTE.render(f'Puntuación: {puntuacion}', True, NEGRO)
    pantalla.blit(puntuacion_texto, (10, 10))

    # Actualizar pantalla
    pygame.display.update()
    reloj.tick(60)

# Salir del juego
pygame.quit()