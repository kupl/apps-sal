def traffic_lights(road, n):
    C, D, res = 0, {i: [c, 0] for i, c in enumerate(road) if c in "GOR"}, [road]

    def updateLights():
        for i, (c, k) in D.items():
            if c == 'G':
                if k == 4:
                    D[i] = ('O', 0)
                else:
                    D[i] = ('G', k + 1)
            elif c == 'O':
                D[i] = ('R', 0)
            elif k == 4:
                D[i] = ('G', 0)
            else:
                D[i] = ('R', k + 1)
    for _ in range(n):
        updateLights()
        if not (C + 1) in D or D[C + 1][0] == 'G':
            C += 1
        res.append(''.join('C' if i == C else D[i][0] if i in D else '.' for i in range(len(road))))
    return res
