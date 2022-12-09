import pygame
from dino_runner.components.obstacle.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class bird(Obstacle):
    def __init__(self, image):
        self.img_bird = BIRD
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

        self.X_POS = 80
        self.Y_POS = 350

    def draw(self.screen):
        if self.index >= 10:
            self.index = 0
        
        self.image = self.img_bird[self.type][self.index //5]
        self.bird_rect = self.image.get_rect()
        self.bird_rect.x = self.X_POS
        self.bird_rect.y = self.Y_POS
        self.step_index +=1

