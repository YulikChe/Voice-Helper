import pygame
import sys
import os

pygame.init()
window = pygame.display.set_mode((1024, 576))
pygame.display.set_caption("App")

bg = pygame.image.load('bg.jpg')
clock = pygame.time.Clock()

def drawDog(dog):
    dog2 = pygame.image.load(dog)
    window.blit(dog2, (10, 10))
    pygame.display.update()

def mainn():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    window.blit(bg, (0, 0))
    clock.tick(30)

    pygame.display.update()