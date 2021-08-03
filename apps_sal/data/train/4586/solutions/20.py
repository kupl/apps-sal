def tv_remote(word):
    l = [['a', 'b', 'c', 'd', 'e', '1', '2', '3'],
         ['f', 'g', 'h', 'i', 'j', '4', '5', '6'],
         ['k', 'l', 'm', 'n', 'o', '7', '8', '9'],
         ['p', 'q', 'r', 's', 't', '.', '@', '0'],
         ['u', 'v', 'w', 'x', 'y', 'z', '_', '/']]
    a = [[l.index(x), x.index(y)] for w in word for x in l for y in x if w in y]
    return (sum([abs(x[0] - y[0]) + abs(x[1] - y[1]) for x, y in zip(a[1:], a[:-1])]) + sum(a[0]) + len(word))
