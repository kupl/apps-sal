dic = {}


def partitions(n, x=None, maxx=None):
    x, maxx = (n, n) if x == None else (x, maxx)
    return sum([dic[(x - i, i)] if (x - i, i) in dic else(0 if dic.update({(x - i, i): partitions(n, x - i, i)}) else dic[(x - i, i)])for i in range(1, min([maxx, x]) + 1)[::-1]]) if x else 1
