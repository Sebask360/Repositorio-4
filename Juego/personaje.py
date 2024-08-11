import pygame 

class Cubo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 200
        self.alto = 50
        self.size = 50
        self.velocidad = 50
        self.color = "blue"
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto)

    def dibujar(self, ventana):
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto)
        pygame.draw.rect(ventana,self.color,self.rect)

    def get_rect(self):
        return pygame.Rect(self.x,self.y,self.ancho,self.alto)
