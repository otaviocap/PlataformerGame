from Constants import *
import pygame

class Goal(pygame.sprite.Sprite):

    def __init__(self, game, pos):
        super().__init__()
        self.game = game
        self.x = pos[0] * TILESIZEMULTI
        self.y = pos[1] * TILESIZEMULTI
        self.startx = pos[0] * TILESIZEMULTI
        self.starty = pos[1] * TILESIZEMULTI
        self.going = True
        self.state = -1
        self.getStates()
        self.updateImage()
        self.time = pygame.time.get_ticks()
        self.animationTimer = pygame.time.get_ticks()
        self.rect = pygame.Rect(self.x, self.y, self.image.get_rect().width, self.image.get_rect().height)
        self.game.goals.add(self)

    
    def getStates(self):
        states = pygame.image.load('../assets/goal.png')
        self.states = []
        pos = [-32,0]
        for i in range(2):
            pos[0] += 32
            self.states.append(states.subsurface(pos, (32, 32)))

    def updateImage(self):
        self.state += 1
        if self.state >= 2:
            self.state = 0
        self.image = pygame.transform.scale(self.states[self.state], (int(self.states[self.state].get_size()[0]*TILESIZEMULTI/1.5), int(self.states[self.state].get_size()[1]*TILESIZEMULTI/1.5)))
        

    def update(self):
        if (pygame.time.get_ticks() - self.time)/1000 > 3:
            self.time = pygame.time.get_ticks()
            self.updateImage()

        if (pygame.time.get_ticks() - self.animationTimer)/1000 > 2:
            self.animationTimer = pygame.time.get_ticks()
            self.going = False if self.going else True



        if (self.going):
            self.y -= .2
        else:
            self.y += .2
        self.rect.y = self.y 
        self.rect.x = self.x
        
            
