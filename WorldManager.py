import os


class WorldManager:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        board = {"meta": {"cursor": [0, 0]}, "board": []}
        for i in range(self.y):
            board["board"].append([])
            for j in range(self.x):
                board["board"][i].append(0)
        self.board = board

    def render(self, frames):
        if frames % 60 == 0:
            os.system("clear")
            x = 0
            y = 0
            for i in self.board["board"]:
                for j in i:
                    if x == self.board["meta"]["cursor"][0] and x == self.board["meta"]["cursor"][1]:
                        print("[" + str(j), end="]")
                    else:
                        print(" " + str(j), end=" ")
                    x = x + 1
                y = y + 1
                print("")

    def get_pos(self):
        return self.board["meta"]["cursor"]

    def set_pos(self, x, y):
        self.get_pos()[0] = x
        self.get_pos()[1] = y
