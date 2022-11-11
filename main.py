import pygame, sys
from pygame.locals import QUIT


def draw_screen(screen, ball_pos):
    bg = pygame.image.load('resources/ns-pygame-bg.jpg')
    screen.blit(bg, (0, 0))
    ball = pygame.image.load('resources/ns-pygame-ball.png')
    ball_sf = ball.get_rect(center=ball_pos)
    screen.blit(ball, ball_sf)
    return ball_pos


def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('Ball Simulator')
    return screen, draw_screen(screen, (100, 100))


def main():
    screen, (center_x, center_y) = init_pygame()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    center_x -= 10
                elif event.key == pygame.K_RIGHT:
                    center_x += 10
                elif event.key == pygame.K_DOWN:
                    center_y += 10
                elif event.key == pygame.K_UP:
                    center_y -= 10
                center_x, center_y = draw_screen(screen, (center_x, center_y))

        pygame.display.update()


main()

