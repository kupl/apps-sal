def langtons_ant(n):

    def ant(n):
        di = 'ULDR'
        tbl = {(0, 0): 0}
        turn = 1
        pos = di[0]
        (x, y) = (0, 0)
        for i in range(n):
            if (x, y) not in tbl.keys():
                tbl[x, y] = 0
            cur = tbl[x, y]
            turn = 1 if cur == 1 else 0
            cur = 0 if cur == 1 else 1
            pos = di[(4 + di.index(pos) + (-1 if turn else 1)) % 4]
            tbl[x, y] = cur
            if pos == 'U':
                y -= 1
            elif pos == 'R':
                x -= 1
            elif pos == 'D':
                y += 1
            elif pos == 'L':
                x += 1
        rez = sum(tbl.values())
        return rez
    if n > 10000:
        y = (n - 10000) % 104
        yy = (n - 10000) // 104
        x = yy * 12 + ant(y + 10000)
    else:
        x = ant(n)
    return x
