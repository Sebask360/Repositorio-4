import pygame
from settings import PLAYER_SIZE, PLAYER_SPEED, PLAYER_COLOR

class Cubo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = PLAYER_SIZE
        self.alto = PLAYER_SIZE
        self.velocidad = PLAYER_SPEED
        self.color = PLAYER_COLOR
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)

    def dibujar(self, ventana):
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        pygame.draw.rect(ventana, self.color, self.rect)

    def get_rect(self):
        return self.rect