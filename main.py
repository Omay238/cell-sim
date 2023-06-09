import pygame
import json

from WorldManager import WorldManager


def main():
    print("Running Cell Sim v1.5.1")

    cells = 25
    cell_size = 25

    pygame.init()
    screen = pygame.display.set_mode((cells * cell_size, cells * cell_size + cell_size))
    pygame.display.set_caption("Cell Sim v1.4.0")
    icon = pygame.image.load("./icon.png")
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()

    with open("./cells.json") as cell_list:
        cell_read = json.load(cell_list)

    world_manager = WorldManager(cells, cells, cell_read, 0.1)

    frames = 0
    key_id = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    key_id = key_id - 1
                if event.key == pygame.K_RIGHT:
                    key_id = key_id + 1
                if key_id < 0:
                    key_id = 0
                elif key_id >= len(cell_read):
                    key_id = len(cell_read)
                if event.key == pygame.K_SPACE:
                    pos = pygame.mouse.get_pos()
                    y = int(pos[1] / cell_size)
                    y = 0 if y < 0 else (cells - 1 if y >= cells else y)
                    if key_id == len(cell_read):
                        world_manager.set(y, int(pos[0] / cell_size), 0)
                    else:
                        world_manager.set(y, int(pos[0] / cell_size),
                                          list(cell_read.keys())[key_id])

        screen.fill("black")

        world_manager.render(screen, pygame, cell_size, key_id)
        if frames % 60 == 0:
            world_manager.update()

        pygame.display.flip()

        clock.tick(60)

        frames += 1


if __name__ == "__main__":
    main()
