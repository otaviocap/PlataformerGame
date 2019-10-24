from enemy import *
from mapLoader import mapLoader
from player import *
from wall import *
from camera import *
import pymunk

class game():

    def __init__(self):
        pygame.init()
        self.speedB = 5
        self.screenSize = (1200, 780)
        self.fps = 60
        self.screen = pygame.display.set_mode(self.screenSize)
        self.screen.set_alpha(128)
        pygame.display.set_caption("Tilemap game")
        self.clock = pygame.time.Clock()
        self.space = pymunk.Space()
        self.space.gravity = 0, -1000


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
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.enemyBullet = pygame.sprite.Group

        for i in self.map.tmdata.objects:
            if i.name == 'wall':
                Wall(self, i.x, i.y, i.width, i.height)
            elif i.name == 'enemy':
                Enemy(i.x, i.y, i.width, i.height)
            elif i.name == 'player':
                self.player = Player(self, i.x, i.y, i.width, i.height)

        self.camera = Camera(self.mapRect.width, self.mapRect.height)

    def gameRun(self):
        self.new()
        while True:
            self.events()
            self.update()
            self.draw()


    def events(self):
        self.space.step(0.02)
        keys = pygame.key.get_pressed()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        self.player.events()

    def update(self):
        self.clock.tick(self.fps)
        self.camera.update(self.player)
        self.enemies.update()
        self.player.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.map.underLayer, self.camera.apply_rect(self.mapRect))
        self.screen.blit(self.player.image, self.camera.apply(self.player))
        for i in self.enemies:
            self.screen.blit(i.image, self.camera.apply(i))
        self.screen.blit(self.map.upperLayer, self.camera.apply_rect(self.mapRect))
        pygame.display.flip()

if __name__ == '__main__':
    a = game()
    a.gameRun()