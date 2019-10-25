import pygame
from Constants import *

class Camera():

    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.camera = pygame.Rect(0,0, self.width, self.height)
        self.screenHeight = SCREEN_SIZE[0]
        self.screenWidth = SCREEN_SIZE[1]

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + int(self.screenWidth / 2) + 130
        y = -target.rect.centery + int(self.screenHeight / 2) - 130
        self.camera = pygame.Rect(x, y, self.width, self.height)

    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)

    def applyPos(self, pos):
        return (pos[0] + self.camera.topleft[0], pos[1] + self.camera.topleft[1])