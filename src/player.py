import pygame
import pymunk


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x=0, y=0, sizeX=10, sizeY=10):
        super().__init__()
        self.direction = 'left'
        self.game = game
        self.image = pygame.image.load('../assets/player.png')
        self.image = pygame.transform.scale(self.image, (self.image.get_size()[0], self.image.get_size()[1]))
        self.rect = pygame.Rect(x, y, self.image.get_rect().width, self.image.get_rect().height)
        self.x = x
        self.y = y
        self.w = sizeX
        self.h = sizeY
        self.speed = 4
        self.cooldown = 0
        self.jumping = False
        self.body = pymunk.Body(1,1666)
        self.body.position = x, y


    def update(self):
        self.move()
        if self.cooldown <= 5:
            self.cooldown = 5
        self.x += self.vx
        self.y += self.vy
        self.rect.x = self.x
        self.collideWall('x')
        self.rect.y = self.y
        self.collideWall('y')


    def move(self):
        self.useSpeed = self.speed
        self.vx, self.vy = 0, 1

        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            self.vx += -self.speed
        if key[pygame.K_d]:
            self.vx += self.speed
        if key[pygame.K_w] and not self.jumping:
            self.vy += -self.speed * 2
            self.jumping = True

    def collideWall(self, dir):
        if dir == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y
                self.jumping = False

    def getImg(self):
        return self.image

    def __transformImgSide(self):
        if self.direction == "left":
            self.image = pygame.transform.flip(self.image, True, False)
        elif self.direction == "right":
            self.image = pygame.transform.flip(self.image, True, False)

    def setDirection(self, direction):
        if not self.direction == direction:
            self.direction = direction
            self.__transformImgSide()

    def resetLocation(self):
        self.x = self.spawnX
        self.y = self.spawnY

    def events(self):
        key = pygame.key.get_pressed()

        if self.cooldown <= 0:
            if key[pygame.K_LEFT]:
                # Bullet('left', self.game.speedB, self.game, self)
                self.setDirection('left')
                self.cooldown = 0
            elif key[pygame.K_RIGHT]:
                # Bullet('right', self.game.speedB, self.game, self)
                self.setDirection('right')
                self.cooldown = 0
            elif key[pygame.K_UP]:
                # Bullet('up', self.game.speedB, self.game, self)
                self.cooldown = 0
            elif key[pygame.K_DOWN]:
                # Bullet('down', self.game.speedB, self.game, self)
                self.cooldown = 0