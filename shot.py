from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        for group in self.containers:
            group.add(self)
        self.radius = SHOT_RADIUS
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, SHOT_RADIUS)

    def update(self, dt):
        self.position += (self.velocity* dt)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)