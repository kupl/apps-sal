def hanoiArray(n):
    initial = [x for x in range(n, 0, -1)]
    tow = [initial, [], []]
    ret = str(tow)

    def move(f, t):
        nonlocal tow, ret
        tow[t].append(tow[f].pop())
        ret = ret + '\n' + str(tow)

    def solve(n, f, h, t):
        if n == 0:
            pass
        else:
            solve(n - 1, f, t, h)
            move(f, t)
            solve(n - 1, h, f, t)

    solve(n, 0, 1, 2)

    return ret
