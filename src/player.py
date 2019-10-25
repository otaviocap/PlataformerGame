import pygame
from Constants import *
vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x=0, y=0, sizeX=10, sizeY=10):
        super().__init__()
        self.direction = 'left'

        self.game = game
        self.image = pygame.image.load('../assets/player.png')
        self.image = pygame.transform.scale(self.image, (int(self.image.get_size()[0]*TILESIZEMULTI/3), int(self.image.get_size()[1]*TILESIZEMULTI/3)))
        self.rect = pygame.Rect(x, y, self.image.get_rect().width, self.image.get_rect().height)
        self.rect.center = (SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2)
        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.jumps = 2
        self.playeracc = 1 * TILESIZEMULTI / 3
        self.playerjump = 30 * TILESIZEMULTI / 3


    def update(self):
        self.acc = vec(0, 1)
        self.events()

        self.acc += self.vel * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos
        self.collideWall()

    def jump_cut(self):
        if self.jumps > 0:
            if self.vel.y < -3:
                self.vel.y = -3

    def jump(self):
        # jump only if standing on a platform
        if self.jumps > 0:
            self.jumps -= 1
            self.vel.y = -self.playerjump


    def collideWall(self):
        '''
        hits = pygame.sprite.spritecollide(self, self.game.walls, False)
        if hits:
            lowest = hits[0]
            for hit in hits:
                if hit.rect.bottom > lowest.rect.bottom:
                    lowest = hit
            if self.pos.y < lowest.rect.centery:
                self.pos.y = lowest.rect.top + .3
                self.vel.y = 0
                self.jumping = False
        '''
        hits = pygame.sprite.spritecollide(self, self.game.walls, False)
        if hits:
            if self.pos.y - hits[0].rect.bottom < 0:
                self.pos.y = hits[0].rect.bottom - self.rect.height
                
            elif self.rect.bottom - hits[0].rect.top > 0:
                self.pos.y = hits[0].rect.bottom + self.rect.width
     
            self.vel.y = 0
            self.jumps = 3

    def __transformImgSide(self):
        if self.direction == "left":
            self.image = pygame.transform.flip(self.image, True, False)
        elif self.direction == "right":
            self.image = pygame.transform.flip(self.image, True, False)
   

    def setDirection(self, direction):
        if not self.direction == direction:
            self.direction = direction
            self.__transformImgSide()

    def events(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_d]:
            self.acc.x = self.playeracc
            self.setDirection('left')
        if key[pygame.K_a]:
            self.acc.x = -self.playeracc
            self.setDirection('right')
        if key[pygame.K_LSHIFT]:
            self.acc.x *= 2
            self.setDirection('right')