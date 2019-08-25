from uni_vars import width, height, win
from random import randint
import pygame


class Pipe:
	def __init__(self, pos):
		self.spacing = 180

		self.x = pos[0]
		self.y1 = pos[1]
		self.width = 50
		self.height1 = randint(10, height//1.4285714286)

		self.y2 = self.height1 + self.spacing
		self.height2 = height - self.y2

		self.color = (133, 203, 45)
		self.collider1 = pygame.Rect((self.x, self.y1, self.width, self.height1))
		self.collider2 = pygame.Rect((self.x, self.y2, self.width, self.height2))

	def collision(self, bird):
		if self.collider1.colliderect(bird.collider) or self.collider2.colliderect(bird.collider):
			return True

	def render(self):
		pygame.draw.rect(win, self.color, (self.x, self.y1, self.width, self.height1))
		pygame.draw.rect(win, self.color, (self.x, self.y2, self.width, self.height2))

	def update(self, speed):
		self.x -= speed

		self.collider1 = pygame.Rect((self.x, self.y1, self.width, self.height1))
		self.collider2 = pygame.Rect((self.x, self.y2, self.width, self.height2))
