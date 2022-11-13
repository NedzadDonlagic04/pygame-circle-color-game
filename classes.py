import pygame
from math import sqrt

class MyClock:
    def __init__(self, fps):
        self.FPS = fps
        self.CLOCK = pygame.time.Clock()
    
    def tick(self):
        self.CLOCK.tick(self.FPS)

class Flower:
    def __init__(self, pos):
        self.CIRCLES = [
            { 'pos': pos, 'color': (255, 255, 255), 'radius': 20 },
            { 'pos': (pos[0] + 35, pos[1]), 'color': (255, 255, 255), 'radius': 25 },
            { 'pos': (pos[0], pos[1] + 35), 'color': (255, 255, 255), 'radius': 25 },
            { 'pos': (pos[0] - 35, pos[1]), 'color': (255, 255, 255), 'radius': 25 },
            { 'pos': (pos[0], pos[1] - 35), 'color': (255, 255, 255), 'radius': 25 }, 
        ]
    
    def pythagoras(self, pos1, pos2):
        a = pos2[0] - pos1[0]
        b = pos2[1] - pos1[1]
        return sqrt(a*a + b*b)
    
    def update(self, state):
        leftClick = pygame.mouse.get_pressed()[0]

        if leftClick:
            mousePos = pygame.mouse.get_pos()
            for circle in self.CIRCLES:
                if self.pythagoras(mousePos, circle['pos']) <= circle['radius'] / 2:
                    circle['color'] = state
                    break
    
    def draw(self, screen):
        for circle in self.CIRCLES:
            pygame.draw.circle(screen, circle['color'], circle['pos'], circle['radius'])

class ColorPicker:
    def __init__(self, pos):

        self.RADIUS = 30
        self.POS = pos

        self.CIRCLES = [
            (255, 0, 0),
            (0, 255, 0),
            (0, 0, 255),
            (255, 255 ,0),
            (0, 255, 255),
            (255, 0, 255)
        ]
    
    def draw(self, screen):
        for i in range(0, len(self.CIRCLES)):
            pygame.draw.circle(screen, self.CIRCLES[i], (self.POS[0] + self.RADIUS * 3 * i,self.POS[1]), self.RADIUS)