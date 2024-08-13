import pygame
from settings import ENEMY_SIZE, ENEMY_SPEED, ENEMY_COLOR

class Enemigo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = ENEMY_SIZE
        self.alto = ENEMY_SIZE
        self.velocidad = ENEMY_SPEED
        self.color = ENEMY_COLOR
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)

    def dibujar(self, ventana):
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        pygame.draw.rect(ventana, self.color, self.rect)
    
    def movimiento(self):
        self.y += self.velocidad
        
    def get_rect(self):
        return self.rect
