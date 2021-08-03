def traffic_lights(road, n):
    empty = '.' * len(road)
    r = [road] + [empty] * n
    l = 10 * (5 * 'G' + 'O' + 5 * 'R')
    for i in range(len(road)):
        if road[i] in l:
            for j in range(n + 1):
                r[j] = r[j][:i] + l[j + l.index(road[i])] + r[j][i + 1:]
    for i in range(n):
        if 'C' in r[i][:-1]:
            c = r[i][:-1].index('C')
            if r[i + 1][c + 1] is 'R' or r[i + 1][c + 1] is 'O':
                r[i + 1] = r[i + 1][:c] + 'C' + r[i + 1][c + 1:]
            else:
                r[i + 1] = r[i + 1][:c + 1] + 'C' + r[i + 1][c + 2:]
    return r
