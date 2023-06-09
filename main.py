import pygame
import json

from WorldManager import WorldManager


def main():
    print("Running Cell Sim v1.4.0")

    cells = 25
    cell_size = 25

    pygame.init()
    screen = pygame.display.set_mode((cells * cell_size, cells * cell_size))
    pygame.display.set_caption("Cell Sim v1.4.0")
    icon = pygame.image.load("./icon.png")
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()

    cell_read = {}
    with open("./cells.json") as cell_list:
        cell_read = json.load(cell_list)

    world_manager = WorldManager(cells, cells, cell_read, 0.1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill("black")

        # render
        world_manager.render(screen, pygame, cell_size)
        # end render

        # logic
        world_manager.update()
        # end logic

        pygame.display.flip()

        clock.tick(1)


if __name__ == "__main__":
    main()
