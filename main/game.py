import pygame
from main.display import Display
from main.pywitch_manager import PyWitchManager
from main.click_manager import ClickManager
from main.zombie import Zombie

class Game():
    def __init__(self):
    
        self.width = 1366
        self.height = 768
        self.tps = 60
        self.clock = pygame.time.Clock()
        
        self.start_display()
        self.start_pywitch()
        self.start_game()
        
        
    def start_display(self):
        self.display = Display(self, self.width, self.height)
        self.display.start()
        
    def start_pywitch(self):
        self.pywitch = PyWitchManager()
        self.pywitch.start()
        
    def start_game(self):
        self.is_running=True
        self.click_manager = ClickManager(self)
        self.zombie_dict = {}
        
        self.zombie_dict[1] = Zombie(self,1,0, 0)
        
        while self.is_running:
            self.clock.tick(self.tps)
            
            for event in pygame.event.get():
                if (
                    event.type == pygame.QUIT or
                    (
                        event.type==pygame.KEYDOWN and
                        event.key==pygame.K_ESCAPE
                    )
                ):
                    self.is_running = False
                    
            self.click_manager.update()
            
            for k, v in self.zombie_dict.items():
                v.update()
                    
            self.display.update()
