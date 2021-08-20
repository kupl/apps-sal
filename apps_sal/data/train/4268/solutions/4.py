def next_num(n):
    mpl = 25
    lpn = 3608528850368400786036725
    if n >= lpn:
        return None
    nl = len(str(n))
    extend = {}
    for i in range(1, mpl + 2):
        if i % 10 == 0:
            extend[i] = {'0'}
        elif i % 5 == 0:
            extend[i] = {'0', '5'}
        elif i % 2 == 0:
            extend[i] = {'0', '2', '4', '6', '8'}
        else:
            extend[i] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    d = {1: {'1', '2', '3', '4', '5', '6', '7', '8', '9'}}
    for l in range(2, 2 + nl):
        d[l] = {p + i for i in extend[l] for p in d[l - 1] if int(p + i) % l == 0}
    d[1].add('0')
    if n >= max(map(int, d[nl])):
        return min(map(int, d[nl + 1]))
    else:
        for i in sorted(map(int, d[nl])):
            if i > n:
                return i
