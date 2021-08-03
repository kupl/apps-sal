class Game():

    def __init__(self, board):
        self.board = board

    def play(self, lines):
        r = set(lines)
        while(len(r) < 2 * self.board * (self.board + 1)):
            flag = False
            for i in range(self.board):
                for j in range(self.board):
                    x = (2 * self.board + 1) * i + j + 1
                    s = {x, x + self.board, x + self.board + 1, x + 2 * self.board + 1}
                    if len(r & s) == 3:
                        r |= s
                        flag = True
                        break
                if flag:
                    break
            if not flag:
                break
        return sorted(r)
