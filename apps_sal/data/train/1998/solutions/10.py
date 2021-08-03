class Solution:
    def __init__(self):
        self.win = [[1, 2, 3], [4, 5, 0]]
        self.lose = [[[1, 2, 3], [5, 4, 0]], [[2, 1, 3], [4, 5, 0]], [[1, 3, 2], [4, 5, 0]],
                     [[3, 0, 1], [4, 2, 5]], [[4, 2, 3], [1, 5, 0]], [[1, 5, 3], [4, 2, 0]]]

    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        s = 0
        if board == self.win:
            return 0
        to = [board]
        path = [board]
        while True:
            s += 1
            t = []
            for x in to:
                tmp = self.move(x)
                for z in tmp:
                    if z not in path:
                        path.append(z)
                        t.append(z)
            for y in t:
                if (y == self.win):
                    return s
                else:
                    for z in self.lose:
                        if z == y:
                            return -1
            to = t
        return -1

    def same(self, x, y):
        for i in range(2):
            for j in range(3):
                if x[i][j] != y[i][j]:
                    return False
        return True

    def copy(self, x):
        r = []
        for y in x:
            r.append(y.copy())
        return r

    def move(self, bd):
        p = self.find(bd)
        r = []
        low = p[0] > 0
        le = p[1] == 0
        re = p[1] == 2
        if not le:
            to = self.copy(bd)
            to[p[0]][p[1]] = bd[p[0]][p[1] - 1]
            to[p[0]][p[1] - 1] = 0
            r.append(to)
        if not re:
            to = self.copy(bd)
            to[p[0]][p[1]] = bd[p[0]][p[1] + 1]
            to[p[0]][p[1] + 1] = 0
            r.append(to)
        if low:
            to = self.copy(bd)
            to[p[0]][p[1]] = bd[p[0] - 1][p[1]]
            to[p[0] - 1][p[1]] = 0
            r.append(to)
        else:
            to = self.copy(bd)
            to[p[0]][p[1]] = bd[p[0] + 1][p[1]]
            to[p[0] + 1][p[1]] = 0
            r.append(to)
        return r

    def find(self, bd):
        for i, x in enumerate(bd):
            if 0 in x:
                return (i, x.index(0))
