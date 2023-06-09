import pygame

from WorldManager import WorldManager


def main():
    print("Running Cell Sim v1.3.1")

    cells = 25
    cell_size = 25

    pygame.init()
    screen = pygame.display.set_mode((cells * cell_size, cells * cell_size))
    clock = pygame.time.Clock()

    world_manager = WorldManager(cells, cells, {
        "e": {
            "color": "brown",
            "name": "Earth",
            "rule": "8>79",
            "states": {
                "w>.": "5ll"
            }
        },
        "w": {
            "color": "blue",
            "name": "Water",
            "rule": "8>79>46",
            "states": {
                "7": "8>7>4/",
                "4": "8>7>4/",
                "9": "8>9>6/",
                "6": "8>9>6/",
                ".>f": "a"
            }
        },
        "f": {
            "color": "orange",
            "name": "Fire",
            "rule": "2>13",
            "states": {}
        },
        "a": {
            "color": "lightblue",
            "name": "Air",
            "rule": "2>13>46",
            "states": {
                "1": "2>1>4/",
                "4": "2>1>4/",
                "3": "2>3>6/",
                "6": "2>3>6/",
                "w>.": "5ww",
                "f>.": "5ww",
                ".>f": "5ww"
            }
        },
        "l": {
            "color": "gray",
            "name": "Wall",
            "rule": "5",
            "states": {}
        }
    }, 0.1)

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
