import Cell
import CellManager
import WorldManager

import time

from pynput import keyboard

keys = {"w": False, "a": False, "d": False, "s": False}


def on_press(key):
    try:
        keys[key.char] = True
    except AttributeError:
        print("", end="")


def on_release(key):
    keys[key.char] = False
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

world = WorldManager.WorldManager(25, 25)

cells = {
    "e": Cell.Cell("8>79>5"),
    "w": Cell.Cell("8>79>46>5"),
    "f": Cell.Cell("2>13>5"),
    "a": Cell.Cell("2>13>46>5"),
    "l": Cell.Cell("5")
}

manager = CellManager.CellManager(world.board, cells)


def main():
    print("Running Physics Sim 1.0.0")
    frames = 0
    while True:
        world.render(frames)
        frames = frames + 1
        if keys["w"] and world.get_pos()[1] > 0:
            world.set_pos(world.get_pos()[0], world.get_pos()[1] - 1)
        elif keys["a"] and world.get_pos()[0] > 0:
            world.set_pos(world.get_pos()[0] - 1, world.get_pos()[1])
        elif keys["s"] and world.get_pos()[1] < 24:
            world.set_pos(world.get_pos()[0], world.get_pos()[1] + 1)
        elif keys["d"] and world.get_pos()[0] < 24:
            world.set_pos(world.get_pos()[0] + 1, world.get_pos()[1])
        time.sleep(1 / 60)


if __name__ == "__main__":
    main()
