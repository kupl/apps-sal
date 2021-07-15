def direction_in_grid(n,m):
    index = 0
    directionByIndex = {0:'U', 1:'R', 2:'D', 3:'L'}
    if n <= m:
        index = (n*2 - 1) % 4
    else:
        index = (m*2) % 4
    return directionByIndex.get(index)
