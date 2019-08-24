import pygame

width, height = 500, 700
title = "Flappy Bird"
background = (102, 192, 227)
running = True
clock = pygame.time.Clock()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption(title)