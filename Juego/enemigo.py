import pygame 

class Enemigo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 70
        self.alto = 70
        self.velocidad = 5
        self.color = "red"
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto)

    def dibujar(self, ventana):
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto)
        pygame.draw.rect(ventana,self.color,self.rect)
    
    def movimiento(self):
        self.y += self.velocidad
        
    def get_rect(self):
        return pygame.Rect(self.x,self.y,self.ancho,self.alto)
