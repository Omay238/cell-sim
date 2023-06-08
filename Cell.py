import random


class Cell:
    def __init__(self, rule):
        self.rule = rule

    def update(self, board, position):
        split_rules = self.rule.split(">")
        for i in split_rules:
            steps = [*i]
            random.shuffle(steps)
            for j in steps:
                print(j)

