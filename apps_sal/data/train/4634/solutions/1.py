def pac_man(N, PM, enemies):
    dims = [[0,N], [0,N]]   # [[minX, maxX], [minY, maxY]]
    for pos in enemies:
        for i,x in enumerate(pos):
            if PM[i] > x: dims[i][0] = max(dims[i][0], x+1)
            else:         dims[i][1] = min(dims[i][1], x)
    return (dims[0][1]-dims[0][0]) * (dims[1][1]-dims[1][0]) - 1
