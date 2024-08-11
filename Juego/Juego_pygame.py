import pygame 
import random
from personaje import Cubo
from enemigo  import Enemigo 

ANCHO = 1000
ALTO = 800
SUELO = 700 
VENTANA = pygame.display.set_mode([ANCHO, ALTO]) 
FPS = 60

pygame.font.init()
fuente = pygame.font.Font(None,36)
jugando = True

reloj = pygame.time.Clock()


tiempo_pasado = 0
tiempo_total = 0
tiempo_entre_enemigos = 1000
cubo = Cubo(100, SUELO - 50)

cubo = Cubo(100, 100)

enemigos = []

enemigos.append(Enemigo(random.randint(0, ANCHO - 50), random.randint(0, ALTO -50)))

def gestionar_teclas(teclas):
    if teclas[pygame.K_w] and cubo.y > 0:
        cubo.y -= cubo.velocidad
    if teclas[pygame.K_s] and cubo.y < SUELO - cubo.size:
        cubo.y += cubo.velocidad
    if teclas[pygame.K_a] and cubo.x > 0:
        cubo.x -= cubo.velocidad
    if teclas[pygame.K_d] and cubo.x < ANCHO - cubo.size:
        cubo.x += cubo.velocidad

while jugando:
    tiempo_global = reloj.tick(FPS)
    tiempo_pasado += reloj.tick(FPS)
    tiempo_total += tiempo_global
    print(tiempo_total)


    eventos = pygame.event.get() 

    teclas = pygame.key.get_pressed()

    gestionar_teclas(teclas)

    for evento in eventos:
        if evento.type == pygame.QUIT: 
            jugando = False  

    if tiempo_pasado > tiempo_entre_enemigos:
        enemigo_x = random.randint(0, ANCHO - 50)
        enemigo_y = random.randint(0, SUELO - 50)
        enemigos.append(Enemigo(enemigo_x, enemigo_y))
        tiempo_pasado = 0

    if tiempo_total > 3000:
        tiempo_entre_enemigos = (tiempo_entre_enemigos - 100)
        tiempo_total = 0

    VENTANA.fill("black")

    pygame.draw.rect(VENTANA, (50, 205, 50), (0, SUELO, ANCHO, ALTO - SUELO))
    cubo.dibujar(VENTANA)

    for enemigo in enemigos[:]:
        if cubo.get_rect().colliderect(enemigo.get_rect()):
            enemigos.remove(enemigo)
        else: 
            enemigo.dibujar(VENTANA)
            enemigo.movimiento()

    texto = f"Tiempo: {tiempo_global / 1000:} segundos."
    superficie_texto = fuente.render(texto, True, (255, 255, 255))
    VENTANA.blit(superficie_texto, (10, 10))

    pygame.display.update()


quit()