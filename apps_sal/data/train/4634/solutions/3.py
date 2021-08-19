def pac_man(N, PM, enemies):
    borders = [[-1, 0], [0, -1], [-1, N - 1], [N - 1, -1], [N, 0], [N, N - 1], [0, N], [N - 1, N]]
    for n in range(1, N - 1):
        borders.append([-1, n])
        borders.append([n, -1])
        borders.append([n, N])
        borders.append([N, n])
    ghosts = []
    for i in enemies:
        x = i[0]
        y = i[1]
        for n in range(N):
            ghosts.append([x, n])
            ghosts.append([n, y])
    possibilities = []
    moved = [PM]
    while moved != []:
        moved2 = moved
        moved = []
        for i in moved2:
            x = i[0]
            y = i[1]
            mon = [[x, y + 1], [x, y - 1], [x + 1, y], [x - 1, y]]
            for m in mon:
                if m not in borders and m not in ghosts:
                    if m not in possibilities and m not in moved and (m != PM):
                        possibilities.append(m)
                        moved.append(m)
    return len(possibilities)
