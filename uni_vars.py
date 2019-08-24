import pygame

width, height = 550, 650
title = "Flappy Bird"
background = (102, 192, 227)
running = True
FPS = 60
clock = pygame.time.Clock()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption(title)