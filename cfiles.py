import pygame

def getcutpic(spritepath,n,scale):
    sprite=pygame.image.load(spritepath)

    images=[]

    w=sprite.get_width()
    h=sprite.get_height()
    rw=w//n

    for i in range(0,w,rw):
        image=sprite.subsurface(i,0,rw,h)
        image=pygame.transform.scale(image,[rw*scale,h*scale])
        images.append(image)
    
    return(images)

def loadimage(imagepath,scale):
    sprite=pygame.image.load(imagepath)

    w=sprite.get_width()
    h=sprite.get_height()

    sprite=pygame.transform.scale(sprite,[w*scale,h*scale])

    return(sprite)

def loadimagesize(imagepath,nx,ny):
    sprite=pygame.image.load(imagepath)

    w=sprite.get_width()
    h=sprite.get_height()

    sprite=pygame.transform.scale(sprite,[nx,ny])

    return(sprite)