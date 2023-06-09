import random


class WorldManager:
    def __init__(self, width, height, types, fill_rate):
        self.width = width
        self.height = height
        self.types = types
        board = []
        for i in range(height):
            board.append([])
            for j in range(width):
                if random.randint(0, 1 / fill_rate) == 1:
                    board[i].append({"type": random.choice(list(types)), "prev": []})
                else:
                    board[i].append(0)
        self.board = board

    def render(self, screen, pygame, size):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[j][i] != 0:
                    pygame.draw.rect(screen, self.types[self.board[j][i]["type"]]["color"],
                                     pygame.Rect(j * size, i * size, size, size))

    def update_cell(self, x, y):
        idx = self.board[x][y]
        if idx != 0:
            idx["prev"] = list(set(idx["prev"]) & set(self.types[idx["type"]]["states"].keys()))
            random.shuffle(idx["prev"])
            if len(idx["prev"]) == 0:
                cell_rules = self.types[idx["type"]]["rule"].split(">")
            else:
                cell_rules = self.types[idx["type"]]["states"][idx["prev"][0]].split(">")
            cell_rules = [''.join(random.sample(string, len(string))) for string in cell_rules]
            move = ""
            for i in cell_rules:
                for j in i:
                    gx = 0
                    gy = 0
                    move = j
                    if j == "1":
                        gx = -1
                        gy = -1
                    elif j == "2":
                        gx = 0
                        gy = -1
                    elif j == "3":
                        gx = 1
                        gy = -1
                    elif j == "4":
                        gx = -1
                        gy = 0
                    elif j == "6":
                        gx = 1
                        gy = 0
                    elif j == "7":
                        gx = -1
                        gy = 1
                    elif j == "8":
                        gx = 0
                        gy = 1
                    elif j == "9":
                        gx = 1
                        gy = 1
                    elif j == "0":
                        self.board[x][y] = 0
                        return True
                    elif j == "/":
                        self.board[x][y]["prev"] = []
                        return True
                    else:
                        if j in self.types.keys():
                            self.board[x][y]["type"] = j
                            self.board[x][y]["prev"].append(j)
                            return True
                    if gx != 0 or gy != 0:
                        ex = x + gx
                        ey = y + gy
                        cx = (True if ex >= 0 else False) if ex < self.width else False
                        cy = (True if ey >= 0 else False) if ey < self.height else False
                        if cx and cy:
                            if self.board[ex][ey] == 0:
                                self.board[x][y]["prev"].append(move)
                                self.board[ex][ey] = self.board[x][y]
                                self.board[x][y] = 0
                            else:
                                self.board[x][y]["prev"].append(f".>{self.board[ex][ey]['type']}")
                                self.board[ex][ey]["prev"].append(f"{self.board[x][y]['type']}>.")
                            return True

            return False

    def update(self):
        failed = []
        for i in range(self.height):
            for j in range(self.width):
                self.update_cell(i, j)
