import pygame

class Animation:
    def __init__(self,images:list[pygame.Surface],period:int):
        self.images=images
        self.period=period
        self.timer=0
        self.index=0

    def render(self,screen:pygame.Surface,x:float,y:float,flip:str):

        if flip=='right':
            screen.blit(self.images[self.index],[x,y])
        else:
            flipimg=pygame.transform.flip(self.images[self.index],True,False)
            screen.blit(flipimg,[x,y])

    def get_size(self):
            imagesize=self.images[self.index].get_size()
            return(imagesize) 

    def update(self):
        self.timer+=1
        if self.timer==self.period:
            self.index+=1
            self.timer=0
        
        if self.index==len(self.images):
            self.index=0
        
