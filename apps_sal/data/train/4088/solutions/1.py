class Game:

    def __init__(self, arr):
        self.comands = arr
        self.score = 0
        self.step = None
        self.fild = [-1] * 9
        self.over = lambda x: max(x) >= 29

    def __break__(self):
        while -1 not in self.fild:
            self.score += 1
            self.fild = [e - 1 for e in self.fild]
        return self.over(self.fild)

    def __values__(self, comand):
        self.step = 4 + {'R': lambda m: +int(m), 'L': lambda m: -int(m)}[comand[1]](comand[2])
        return int(comand[0])

    def game(self):
        for comand in self.comands:
            block = self.__values__(comand)
            self.fild[self.step] += block
            if self.__break__():
                break
        return self.score


def tetris(arr) -> int:
    play = Game(arr)
    return play.game()
