# Import modules
import pygame
pygame.init()
pygame.font.init()

# Import classes and variables from other files
from uni_vars import width, height, win, running, framecount, message, clock, FPS, background
from bird import Bird
from pipe import Pipe


class FlappyBird:
	def start(self):
		self.player = Bird((width/2, height/2))
		self.pipes = []

		self.pipes.append(Pipe((width, 0)))

	def logic(self):
		global running, framecount
		framecount += 1
		self.player.x_vel += 0.0001

		# Obstacle regeneration
		if framecount % 200 == 0:
			self.pipes.append(Pipe((width, 0)))

		# Scoring
		if framecount % 10 == 0:
			self.player.score += 1

		keys = pygame.key.get_pressed()
		space = keys[pygame.K_SPACE]
		up = keys[pygame.K_UP]
		if space or up:
			if self.player.y_vel > 4:
				self.player.flap()

		self.player.update()

		for pipe in self.pipes:
			if pipe.collision(self.player):
				running = False

			pipe.update(self.player.x_vel)

			if pipe.x + pipe.width < 0:
				self.pipes.remove(pipe)

		if self.player.y - self.player.radius < 0:
			self.player.y_vel = 0
			self.player.y = self.player.radius
		if self.player.y - self.player.radius*5 > width:
			running = False

	def render(self):
		for pipe in self.pipes:
			pipe.render()

		self.player.render()
		message(str(self.player.score), (255, 255, 255), (width/2-50*0.35, 5))








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
