import pygame 
import random
from player import Cubo
from enemy import Enemigo
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_HEIGHT, FPS, ENEMY_SPAWN_TIME, BACKGROUND_COLOR

VENTANA = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

pygame.font.init()
fuente = pygame.font.Font(None, 36)
jugando = True

reloj = pygame.time.Clock()

tiempo_pasado = 0
tiempo_total = 0
tiempo_entre_enemigos = ENEMY_SPAWN_TIME
cubo = Cubo(100, GROUND_HEIGHT - 50)

enemigos = []
enemigos.append(Enemigo(random.randint(0, SCREEN_WIDTH - 50), random.randint(0, SCREEN_HEIGHT - 50)))

def gestionar_teclas(teclas):
    if teclas[pygame.K_w] and cubo.y > 0:
        cubo.y -= cubo.velocidad
    if teclas[pygame.K_s] and cubo.y < GROUND_HEIGHT - cubo.size:
        cubo.y += cubo.velocidad
    if teclas[pygame.K_a] and cubo.x > 0:
        cubo.x -= cubo.velocidad
    if teclas[pygame.K_d] and cubo.x < SCREEN_WIDTH - cubo.size:
        cubo.x += cubo.velocidad

while jugando:
    tiempo_global = reloj.tick(FPS)
    tiempo_pasado += tiempo_global
    tiempo_total += tiempo_global

    eventos = pygame.event.get() 
    teclas = pygame.key.get_pressed()

    gestionar_teclas(teclas)

    for evento in eventos:
        if evento.type == pygame.QUIT: 
            jugando = False  

    if tiempo_pasado > tiempo_entre_enemigos:
        enemigo_x = random.randint(0, SCREEN_WIDTH - 50)
        enemigo_y = random.randint(0, GROUND_HEIGHT - 50)
        enemigos.append(Enemigo(enemigo_x, enemigo_y))
        tiempo_pasado = 0

    if tiempo_total > 3000:
        tiempo_entre_enemigos -= 100
        tiempo_total = 0

    VENTANA.fill(BACKGROUND_COLOR)

    pygame.draw.rect(VENTANA, (50, 205, 50), (0, GROUND_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT - GROUND_HEIGHT))
    cubo.dibujar(VENTANA)

    for enemigo in enemigos[:]:
        if cubo.get_rect().colliderect(enemigo.get_rect()):
            enemigos.remove(enemigo)
        else: 
            enemigo.dibujar(VENTANA)
            enemigo.movimiento()

    texto = f"Tiempo: {tiempo_global / 1000:.2f} segundos."
    superficie_texto = fuente.render(texto, True, (255, 255, 255))
    VENTANA.blit(superficie_texto, (10, 10))

    pygame.display.update()

pygame.quit()