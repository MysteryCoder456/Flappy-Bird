# Import classes and variables from other files
from uni_vars import *

# Import modules
import pygame


class FlappyBird:
	def start(self):
		pass

	def logic(self):
		pass

	def render(self):
		pass


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
