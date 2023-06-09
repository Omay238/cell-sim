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
                        board[i].append({"type": random.choice(list(types)), "prev": [], "moved_last": False})
                else:
                    board[i].append(0)
        self.board = board

    def render(self, screen, pygame, size, highlight):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[j][i] != 0:
                    pygame.draw.rect(screen, self.types[self.board[j][i]["type"]]["color"],
                                     pygame.Rect(j * size, i * size, size, size))
        for i in range(len(self.types.keys())):
            pygame.draw.rect(screen, self.types[list(self.types.keys())[i]]["color"],
                             pygame.Rect(i * size, self.height * size, size, size))
        pygame.draw.rect(screen, "white", pygame.Rect(highlight * size, self.height * size, size, size),
                         int(size * 0.2))

    def update_cell(self, x, y):
        idx = self.board[x][y]
        if idx != 0 and not idx["moved_last"]:
            idx["prev"] = list(set(idx["prev"]) & set(self.types[idx["type"]]["states"].keys()))
            random.shuffle(idx["prev"])
            if len(idx["prev"]) == 0:
                cell_rules = self.types[idx["type"]]["rule"].split(">")
            else:
                cell_rules = self.types[idx["type"]]["states"][idx["prev"][0]].split(">")
            cell_rules = [''.join(random.sample(string, len(string))) for string in cell_rules]
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
                        return x, y
                    else:
                        if j in self.types.keys():
                            self.board[x][y]["type"] = j
                            self.board[x][y]["prev"].append(j)
                            return x, y
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
                                overrides = self.types[idx["type"]]["overrides"]
                                goal_type = self.board[ex][ey]["type"]
                                if goal_type in overrides.keys():
                                    if overrides[goal_type] == "swap":
                                        self_copy = self.board[x][y]
                                        self.board[x][y] = self.board[ex][ey]
                                        self.board[ex][ey] = self_copy
                                    elif overrides[goal_type] == "remove":
                                        self.board[ex][ey] = self.board[x][y]
                                    elif overrides[goal_type] == "push":
                                        self_copy = self.board[x][y]
                                        self.board[x][y] = self.board[ex][ey]
                                        self.board[ex][ey] = self_copy
                            return ex, ey
            return False

    def update(self):
        failed = []
        for i in range(self.height):
            for j in range(self.width):
                success = self.update_cell(i, j)
                failed.append((i, j)) if not success else print("", end="")
                if success:
                    self.board[success[0]][success[1]]["moved_last"] = True
        for i in self.board:
            for j in i:
                if j != 0:
                    j["moved_last"] = False

    def set(self, x, y, cell_type):
        if cell_type == 0:
            self.board[y][x] = 0
        else:
            self.board[y][x] = {"type": cell_type, "prev": [], "moved_last": False}
