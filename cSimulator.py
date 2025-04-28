from random import randint

from cParticle import Particle

class Simulator:
    def __init__(self, num_particles, height, width):
        self._particles = self.initialize_particles(num_particles)
        self.height = height
        self.width = width

    @property
    def particles(self):
        return self._particles

    def initialize_particles(self, num_particles):
        # Create the particles using the Particle class.
        particles = []
        color = [(79, 187, 224), (255, 255, 255), (255, 111, 81)]
        for i in range(0, num_particles):
            pos = (randint(50, 400), randint(50, 400))
            speed = randint(4, 6)
            radius = 5
            particles.append(Particle(pos, (1, 1), speed, radius, color[i%3]))
        
        return particles
  
    def simulate(self):
        # Perform guidance alterations to particle direction.
        for particle in self._particles:
            particle.guidance([0, self.width, 0, self.height], self._particles)
            particle.update_pos()
  
        return self._particles