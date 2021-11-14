import pygame
import math
import random
import time

class Zombie():
    def __init__(self, game, ent_id, x, y):
        self.game = game
        self.ent_id = ent_id
        self.x = x
        self.y = y
        self.v = 0.5
        self.vx=0
        self.vy=0
        self.radius=15
        self.contact_radius_sq = 25*25
        self.colour = (0,150,0,255)

        self.sprite=pygame.Surface(
            (2*self.radius, 2*self.radius), pygame.SRCALPHA
        )
        self.sprite.fill((0,0,0,0))
        pygame.draw.circle(
            self.sprite, self.colour,
            (self.radius, self.radius), self.radius
        )
        
    def update(self):
        ctime=time.time()
        cx = 1366/2.
        cy = 768/2.
        dx = cx-self.x
        dy = cy-self.y
        angle = math.atan2(dy, dx)

        self.vx = self.v*math.cos(angle)
        self.vy = self.v*math.sin(angle)
        
        self.x+=self.vx
        self.y+=self.vy
        
        for k, v in self.game.click_manager.click.items():
            if ctime > v['etime']:
                continue
            ddx = self.x-v['x']
            ddy = self.y-v['y']
            dr = ddx*ddx+ddy*ddy
            
            if dr < self.contact_radius_sq:
                dangle = math.pi*2*random.random()
                self.x = cx + cx * math.cos(dangle)
                self.y = cy + cy * math.sin(dangle)
            
        
    def draw(self):
        self.game.display.blit(self.sprite, (self.x-self.radius, self.y-self.radius))
