import pygame

class Camera():

    def __init__(self, height, width):
        self.camera = pygame.Rect(0,0, width, height)
        self.width = width
        self.height = height
        self.screenHeight = 1200
        self.screenWidth = 720

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + int(self.screenWidth / 2)
        y = -target.rect.centery + int(self.screenHeight / 2)
        self.camera = pygame.Rect(x, y, self.width, self.height)

    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)

    def applyPos(self, pos):
        return (pos[0] + self.camera.topleft[0], pos[1] + self.camera.topleft[1])