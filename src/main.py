from Goal import *
from MapLoader import mapLoader
from Player import *
from Wall import *
from Camera import *
from Constants import *
import pygame
import random

class game():

    def __init__(self):
        pygame.init()
        self.screenSize = SCREEN_SIZE
        self.fps = FPS
        self.screen = pygame.display.set_mode(self.screenSize)
        self.screen.set_alpha(128)
        pygame.display.set_caption(SCREEN_TITLE)
        self.clock = pygame.time.Clock()
        self.time = pygame.time.get_ticks()


    def new(self):
        try:
            self.mapPath = '../assets/map1.tmx'
            self.map = mapLoader(self.mapPath)
        except:
            self.mapPath = '../assets\\map1.tmx'
            self.map = mapLoader(self.mapPath)

        self.mapImg = self.map.makeMap(self)
        self.mapRect = self.mapImg.get_rect()
        self.frontSprites = pygame.sprite.Group()
        self.backSprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.goals = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.positions = []

        for i in self.map.tmdata.objects:
            if i.name == 'wall':
                Wall(self, i.x * TILESIZEMULTI, i.y * TILESIZEMULTI, i.width * TILESIZEMULTI, i.height * TILESIZEMULTI)
            elif i.name == 'goal':
                self.positions.append((i.x, i.y))
            elif i.name == 'player':
                self.player = Player(self, i.x * TILESIZEMULTI, i.y * TILESIZEMULTI, i.width, i.height)

        self.camera = Camera(self.mapRect.width, self.mapRect.height)

    def gameRun(self):
        self.new()
        while True:
            self.events()
            self.update()
            self.draw()


    def events(self):
        keys = pygame.key.get_pressed()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_w:
                    self.player.jump()
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_w:
                    self.player.jump_cut()
        
        if (len(self.goals) == 0 or (self.time - pygame.time.get_ticks()) / 1000 > 5):
            Goal(self, random.choice(self.positions))

        self.player.events()

    def update(self):
        self.clock.tick(self.fps)
        self.camera.update(self.player)
        self.goals.update()
        self.player.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.map.underLayer, self.camera.apply_rect(self.mapRect))
        self.screen.blit(self.player.image, self.camera.apply(self.player))
        for i in self.goals:
            self.screen.blit(i.image, self.camera.apply(i))
        self.screen.blit(self.map.upperLayer, self.camera.apply_rect(self.mapRect))
        pygame.display.flip()

if __name__ == '__main__':
    a = game()
    a.gameRun()