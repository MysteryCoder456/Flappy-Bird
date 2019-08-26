from uni_vars import win, gravity
import pygame


class Bird:
	def __init__(self, pos):
		self.x = pos[0]
		self.y = pos[1]
		self.radius = 20
		self.color = (247, 191, 37)
		self.draw_x = self.x - self.radius
		self.draw_y = self.y - self.radius
		self.x_vel = 2
		self.y_vel = 0
		self.flap_power = 15
		self.collider = pygame.Rect((self.draw_x, self.draw_y, self.radius*2, self.radius*2))
		self.score = 0

	def flap(self):
		self.y_vel = -self.flap_power

	def render(self):
		pygame.draw.ellipse(win, self.color, (self.draw_x, self.draw_y, self.radius*2, self.radius*2))

	def update(self):
		# Acceleration
		self.y_vel += gravity

		# Movement
		self.y += self.y_vel

		# Updating rendering coordinates
		self.draw_x = self.x - self.radius
		self.draw_y = self.y - self.radius

		# Update colliders
		self.collider = pygame.Rect((self.draw_x, self.draw_y, self.radius*2, self.radius*2))
