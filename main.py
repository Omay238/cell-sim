import pygame

import WorldManager
import CellManager
import Cell


def main():
    print("Running Cell Sim v2.0.0")
    pygame.init()
    screen = pygame.display.set_mode((720, 720))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill("black")

        # render

        # end render

        # logic

        # end logic

        pygame.display.flip()

        clock.tick(60)


if __name__ == "__main__":
    main()