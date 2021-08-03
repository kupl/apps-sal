class Game():

    def __init__(self, board):
        self.board = board

    def internal(self, lines):
        result = set()
        retval = False
        pts_per_line = (self.board * 2) + 1
        for by in range(self.board):
            for bx in range(self.board):
                h1 = 1 + (by * pts_per_line) + bx
                h2 = (h1 + pts_per_line)
                v1 = (h1 + self.board)
                v2 = (v1 + 1)

                count = 0
                if h1 in lines:
                    count += 1
                    result.add(h1)
                if h2 in lines:
                    count += 1
                    result.add(h2)
                if v1 in lines:
                    count += 1
                    result.add(v1)
                if v2 in lines:
                    count += 1
                    result.add(v2)

                if count == 3:
                    retval = True
                    result.add(h1)
                    result.add(h2)
                    result.add(v1)
                    result.add(v2)

        ret = list(result)
        ret.sort()
        return ret, retval

    def play(self, lines):
        cont = True
        while cont:
            ret, cont = self.internal(lines)
            lines = ret
        return lines
