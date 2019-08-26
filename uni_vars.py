import pygame

width, height = 600, 700
title = "Flappy Bird"
background = (102, 192, 227)
running = True
FPS = 60
clock = pygame.time.Clock()
font = pygame.font.SysFont('Comic Sans MS', 50)
win = pygame.display.set_mode((width, height))
pygame.display.set_caption(title)

# gameplay variables
gravity = 1
framecount = 0

# gameplay functions
def message(content, color, position):
		screen_text = font.render(content, True, color)
		win.blit(screen_text, position)
