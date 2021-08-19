class Funnel(object):

    def __init__(self):
        self.data = [[None for _ in range(row + 1)] for row in range(5)]

    def fill(self, *args):
        if args:
            for row in self.data:
                for (i, val) in enumerate(row):
                    if val == None:
                        (row[i], args) = (args[0], args[1:])
                        if not args:
                            return

    def __weight(self, pos, hist):
        if pos in hist:
            return 0
        (y, x) = pos
        if not (0 <= y < len(self.data) and 0 <= x < len(self.data[y])):
            return 0
        hist.append(pos)
        return 0 if self.data[y][x] == None else 1 + sum((self.__weight(p, hist) for p in ((y + 1, x), (y + 1, x + 1))))

    def drip(self):
        ret = self.data[0][0]
        pos = (0, 0)
        top = [(1, 0), (1, 1)]
        while True:
            top = [(pos[0] + 1, pos[1] + i) for i in range(2)]
            top = [(x, self.__weight(x, [])) for x in top]
            top = list([x for x in top if x[1] != 0])
            if not top:
                if pos == (0, 0):
                    self.data[pos[0]][pos[1]] = None
                return ret
            top.sort(key=lambda x: x[1], reverse=True)
            t_pos = top[0][0]
            self.data[pos[0]][pos[1]] = self.data[t_pos[0]][t_pos[1]]
            self.data[t_pos[0]][t_pos[1]] = None
            pos = t_pos

    def __str__(self):

        def str_row(r):
            return str(r).replace('[', '\\').replace(']', '/').replace(',', '').replace('None', ' ').replace("'", '').center(11, ' ').rstrip()
        return '\n'.join((str_row(row) for row in self.data[::-1]))
