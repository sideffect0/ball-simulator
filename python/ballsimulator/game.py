import sys
import time
import pygame
from pygame.locals import QUIT
from random import randint

game_clock = pygame.time.Clock()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
BALL_SIZE = 10
BOUND_X = WINDOW_WIDTH - BALL_SIZE
BOUND_Y = WINDOW_HEIGHT - BALL_SIZE
DELTA = 10
FPS = 60

class Ball(object):
    def __init__(self):
        self.pos = (randint(0, WINDOW_WIDTH - BALL_SIZE), randint(0, WINDOW_HEIGHT - BALL_SIZE))
        self.velX, self.velY = (max(1, randint(-4, 4)), max(1, randint(-4, 4)))
        self.ball = pygame.image.load('resources/ns-pygame-ball.png');

    def render(self, screen):
        ball_sf = self.ball.get_rect(center=self.pos)
        screen.blit(self.ball, ball_sf)

    def move(self):
        x,y = self.pos
        if x <= 0 or x >= BOUND_X:
            self.velX = -self.velX
        if y <= 0 or y >= BOUND_Y:
            self.velY = -self.velY
        self.pos = (x + (DELTA*self.velX), y + (DELTA*self.velY))

class Window(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.bg = pygame.image.load('resources/ns-pygame-bg.jpg')
        pygame.display.set_caption('Ball Simulator')
        self.balls = [Ball() for _ in range(7)]

    def render(self):
        self.screen.blit(self.bg, (0, 0))
        for ball in self.balls:
            ball.move()
            ball.render(self.screen)

def start():
    window = Window()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        window.render()         
        pygame.display.update()
        game_clock.tick(FPS)
        # time.sleep(0.1)

