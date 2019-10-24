import pygame
import pytmx


class mapLoader:

    def __init__(self, file):
        tm = pytmx.load_pygame(file, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmdata = tm


    def render(self, surface, game):
        ti = self.tmdata.get_tile_image_by_gid
        tempSurface2 = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
        tempSurface3 = pygame.Surface(surface.get_size())
        for layers in self.tmdata.visible_layers:
            if layers.name == 'Foreground':
                if isinstance(layers, pytmx.TiledTileLayer):
                    for x, y, gid in layers:
                        tile = ti(gid)
                        if tile:
                            if gid == 0:
                                pass
                            else:
                                tempSurface2.blit(tile, (x * self.tmdata.tilewidth, y * self.tmdata.tileheight))
                    self.upperLayer = tempSurface2
                    
            elif isinstance(layers, pytmx.TiledTileLayer):
                for x, y, gid in layers:
                    tile = ti(gid)
                    if tile:
                        tempSurface3.blit(tile, (x * self.tmdata.tilewidth, y * self.tmdata.tileheight))
                self.underLayer = tempSurface3


    def makeMap(self, game):
        tempSurface = pygame.Surface((self.width, self.height))
        self.render(tempSurface, game)
        return tempSurface

    def getProportions(self):
        return (self.height, self.width)
