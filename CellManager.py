class CellManager:
    def __init__(self, board, cells):
        self.board = board
        self.cells = cells

    def update(self):
        for i in self.board["board"]:
            for j in i:
                print("")
