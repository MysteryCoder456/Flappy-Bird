# Import classes and variables from other files
from uni_vars import *
from bird import Bird

# Import modules
import pygame


class FlappyBird:
	def start(self):
		self.player = Bird((width/2, height/2))

	def logic(self):
		keys = pygame.key.get_pressed()
		space = keys[pygame.K_SPACE]
		up = keys[pygame.K_UP]
		if space or up:
			if self.player.y_vel > 4:
				self.player.flap()

		self.player.update()

		if self.player.y - self.player.radius < 0:
			self.player.y_vel = 0
		if self.player.y - self.player.radius*5 > width:
			global running
			running = False

	def render(self):
		self.player.render()









# ############################################# #
# ### DO NOT TOUCH ANY CODE BELOW THIS LINE ### #
# ############################################# #








def main():
	global running

	game = FlappyBird()
	game.start()

	while running:
		clock.tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		game.logic()
		win.fill(background)
		game.render()
		pygame.display.update()


if __name__ == "__main__":
	main()
	pygame.quit()
	quit()
