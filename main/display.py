import pygame


class Display():
    def __init__(self,game, width, height):
        self.game = game
        self.w = width
        self.h = height
        
    def start(self):
        self.display = pygame.display.set_mode(
            (self.w, self.h), pygame.DOUBLEBUF
        )
        
    def blit(self,*args, **kwargs):
        self.display.blit(*args, **kwargs)
        
    def update(self):
        self.display.fill((0,0,255))

        if hasattr(self.game,'click_manager'):
            self.game.click_manager.draw()
                
        if hasattr(self.game,'zombie_dict'):
            for k, v in self.game.zombie_dict.items():
                v.draw()
        
        pygame.display.flip()
