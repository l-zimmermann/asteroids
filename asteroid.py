import pygame.draw

from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        centerPos = self.position.x, self.position.y
        pygame.draw.circle(screen, color="white",center=centerPos, radius=self.radius, width=2)

    def update(self, dt):
        self.position += dt * self.velocity
