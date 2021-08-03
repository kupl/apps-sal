def check(lst, row, col):
    rows = [i for i in [-1, -2, -3, -4, -5] if i < row - 1]
    idx1 = (row - 1, col)
    val1 = lst[row - 1][col]
    try:
        idx2 = (row - 1, col + 1)
        val2 = lst[row - 1][col + 1]
    except:
        return idx1
    c1, w = 0, 2
    for i in rows:
        for j in range(col, col + w):
            try:
                if lst[i][j] != " ":
                    c1 += 1
            except:
                pass
        w += 1
    c2, w = 0, 2
    for i in rows:
        for j in range(col + 1, col + 1 + w):
            try:
                if lst[i][j] != " ":
                    c2 += 1
            except:
                pass
        w += 1
    if val1 == " " and val2 != " ":
        return idx2
    if val1 != " " and val2 == " ":
        return idx1
    if val1 != " " and val2 == " ":
        return idx1
    if c1 >= c2:
        return idx1
    if c2 > c1:
        return idx2


class Funnel(object):
    def __init__(self):
        self.lst = [[" ", " ", " ", " ", " "],
                    [" ", " ", " ", " "],
                    [" ", " ", " "],
                    [" ", " "],
                    [" "]]

    def fill(self, *args):
        args = list(args)
        if args != []:
            for i in [-1, -2, -3, -4, -5]:
                c = abs(i)
                x = self.lst[i]
                f = False
                for j in range(c):
                    if x[j] == " ":
                        x[j] = args.pop(0)
                        if args == []:
                            f = True
                            break
                self.lst[i] = x
                if f == True:
                    break
            return self.lst
        return self.lst

    def drip(self):
        if self.lst[-1][-1] != " ":
            val = self.lst[-1][-1]
            self.lst[-1][-1] = " "
            idx = 0
            for i in [-1, -2, -3, -4]:
                res = check(self.lst, i, idx)
                self.lst[i][idx] = self.lst[res[0]][res[1]]
                self.lst[res[0]][res[1]] = " "
                idx = res[1]
            return val

    def __str__(self):
        res = [" " * (i) + "\\" + ' '.join(list(map(str, e))) + "/" for i, e in enumerate(self.lst)]
        return '\n'.join(res)
