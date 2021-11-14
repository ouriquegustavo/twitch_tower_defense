import pygame
import time
import random

class ClickManager():
    def __init__(self,game):
        self.game=game
        self.click = {}
        self.last_event_id = ''
        self.radius=20
        self.max_time=10
        self.colour=(255,0,0,255)
        self.sprite=pygame.Surface(
            (2*self.radius, 2*self.radius), pygame.SRCALPHA
        )
        self.sprite.fill((0,0,0,0))
        pygame.draw.circle(
            self.sprite, self.colour,
            (self.radius, self.radius), self.radius
        )
        
    def update(self):
        ctime = time.time()
        event_id = self.game.pywitch.data_click.get('event_id')
        display_name = self.game.pywitch.data_click.get('display_name')
        if event_id and display_name and event_id != self.last_event_id:
            self.last_event_id = event_id
            colour = self.click.get(display_name,{}).get('colour')
            if not colour:
                colour = (
                    random.randint(0,255),
                    random.randint(0,255),
                    random.randint(0,255),
                    255
                )
            data = {
                'x': self.game.pywitch.data_click['x']*self.game.display.w,
                'y': self.game.pywitch.data_click['y']*self.game.display.h,
                'display_name': self.game.pywitch.data_click['display_name'],
                'time': ctime,
                'etime': ctime+self.max_time,
                'colour': colour
            }
            self.click[display_name]=data
            
    def draw(self):
        ctime = time.time()
        for k, v in self.click.items():
            if ctime > self.click[k]['etime']:
                continue
            xpos = v['x']
            ypos = v['y']
            pygame.draw.circle(
                self.sprite, v['colour'],
                (self.radius, self.radius), self.radius
            )
            self.game.display.blit(self.sprite, (xpos-self.radius, ypos-self.radius))
            
