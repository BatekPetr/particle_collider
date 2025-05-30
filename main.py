# Creating a particle collider and exploring visualisation in Pygame.

import pygame
from class_Particle import Particle
from random import randint
from sys import exit

def main():
	# Initialising Pygame window, caption and clock.
	pygame.init()
	WIDTH, HEIGHT = 450, 450
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Particle Collider")
	clock = pygame.time.Clock()

	# Creating the background surface.
	bg = pygame.Surface((WIDTH, HEIGHT))
	bg.fill((20, 20, 20))

	# Create the particles using the Particle class.
	particles = []
	color = [(79, 187, 224), (255, 255, 255), (255, 111, 81)]
	for i in range(0, 1000):
		pos = (randint(50, 400), randint(50, 400))
		speed = randint(4, 6)
		radius = 5
		particles.append(Particle(pos, (1, 1), speed, radius, color[i%3]))

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

		screen.blit(bg, (0, 0))

		# Draw the particles.
		for particle in particles:
			pygame.draw.circle(screen, particle.color, particle.pos, particle.radius)

		# Perform guidance alterations to particle direction.
		for particle in particles:
			particle.guidance([0, WIDTH, 0, HEIGHT], particles)

		# Update the positions of the particles.
		for particle in particles:
			particle.update_pos()

		pygame.display.update()
		clock.tick(30)
	

if __name__ == "__main__":
	main()
