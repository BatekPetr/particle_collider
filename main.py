# Creating a particle collider and exploring visualisation in Pygame.

import pygame
import cSimulator

from sys import exit

NUM_PARTICLES = 500
WIDTH, HEIGHT = 450, 450


def main():
    # Initialising Pygame window, caption and clock.
    pygame.init()
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Particle Collider")
    clock = pygame.time.Clock()

    # Creating the background surface.
    bg = pygame.Surface((WIDTH, HEIGHT))
    bg.fill((20, 20, 20))

    # create particle simulator
    particle_simulator = cSimulator.Simulator(NUM_PARTICLES, HEIGHT, WIDTH)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.blit(bg, (0, 0))

        # Draw the particles.
        for particle in particle_simulator.particles:
            pygame.draw.circle(screen, particle.color, particle.pos, particle.radius)

        # Perform guidance alterations to particle direction.
        particle_simulator.simulate()

        # Update the positions of the particles.
        #for particle in particles:
        #	particle.update_pos()

        pygame.display.update()
        clock.tick(30)
    

if __name__ == "__main__":
    main()
