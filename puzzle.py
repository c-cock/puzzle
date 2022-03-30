import pygame
import random

SCREEN_WIDTH = 420
SCREEN_HEIGHT = 420
FPS = 60

NUM_HORIZONTAL_PANELS = 4
NUM_VERTICAL_PANELS = 5

PANEL_WIDTH = SCREEN_WIDTH / NUM_HORIZONTAL_PANELS
PANEL_HEIGHT = SCREEN_HEIGHT / NUM_VERTICAL_PANELS

def initialize_panels(panels):
    font = pygame.font.SysFont('Arial', 30)

    for y in range(NUM_VERTICAL_PANELS):
        horizontal_panels = []

        for x in range(NUM_HORIZONTAL_PANELS):
            panel = None

            if x != NUM_HORIZONTAL_PANELS - 1 or \
               y != NUM_VERTICAL_PANELS - 1:
                number = y * NUM_HORIZONTAL_PANELS + x + 1

                image = pygame.Surface((PANEL_WIDTH, PANEL_HEIGHT))
                image.fill((255, 255, 255))
                pygame.draw.rect(image, (0, 0, 0), \
                                 (0, 0, PANEL_WIDTH, PANEL_HEIGHT), 3)
                text = font.render(str(number), True, (0, 0, 0))
                (text_width, text_height) = text.get_size()

                pygame.Surface.blit(image, text,\
                                    ((PANEL_WIDTH - text_width) / 2, \
                                     (PANEL_HEIGHT - text_height) / 2))

                panel = {
                    'number': number,
                    'image': image
                }

            horizontal_panels.append(panel)

        panels.append(horizontal_panels)

def main():
    pygame.init()
    pygame.display.set_caption('Puzzle')
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH,
                                           SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    panels = []
    initialize_panels(panels)
    canceled = False

    while not canceled:

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

main()
