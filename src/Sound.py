import pygame
import os.path
import random

class Sound:

    def __init__(self):
        self.sounds = {
            "Jump": [
                self.getSound("jumps", "jump_01.wav"),
                self.getSound("jumps", "jump_02.wav"),
                self.getSound("jumps", "jump_03.wav")
            ],
            "Collect": [
                self.getSound("collect", "01.wav"),
                self.getSound("collect", "02.wav")
            ],
            "Music": [
                self.getSound("music", "01.wav")
            ]
        }

    def getSound(self, sound, filename):
        try:
            a = pygame.mixer.Sound(os.path.join("../assets/", sound, filename))
        except:
            a = pygame.mixer.Sound(os.path.join("assets/", sound, filename))
        return a


    def play(self, sound):
        s = random.choice(self.sounds[sound])
        s.play()

    def playMusic(self):
        s = random.choice(self.sounds["Music"])
        s.set_volume(.5)
        s.play(loops=-1)
