from dino_runner.utils.constants import SCREEN_WIDTH
from pygame.sprite import Sprite

class Obstacle():
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
        #self.obstacle_overcome = 0

    def update(self, game_speed, obstacles):
        self.rect.x = self.rect.x - game_speed
        if self.rect.x < - self.rect.width:
            obstacles.pop()
            #if obstacles.pop(): ##Prueba
            #    self.obstacle_overcome += 1 ##Prueba

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)

        
