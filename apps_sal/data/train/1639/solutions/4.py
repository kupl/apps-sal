from math import factorial as fac


def gta(limit, *args):
    x = [str(i) for i in args]
    y = set()
    while len(y) != limit:
        for i in range(len(args)):
            if x[i] != None:
                if len(x[i]) != 0:
                    y.add(int(x[i][0]))
                if len(x[i]) == 1:
                    x[i] = None
                elif len(x[i]) == 2:
                    x[i] = x[i][1]
                else:
                    x[i] = x[i][1:]
                if len(y) == limit:
                    break
    y, l = list(y), len(y)
    tot = [fac(l) / fac(i) * (sum(y) * 1.0 / l) * (l - i) for i in range(l)]
    return round(sum(tot), 0)
