def solomons_quest(arr):
    layer = 0
    coord = [0, 0]
    for i in arr:
        layer = layer + i[0]
        if i[1] == 0:
            coord[1] = coord[1] + i[2] * 2 ** layer
        if i[1] == 1:
            coord[0] = coord[0] + i[2] * 2 ** layer
        if i[1] == 2:
            coord[1] = coord[1] - i[2] * 2 ** layer
        if i[1] == 3:
            coord[0] = coord[0] - i[2] * 2 ** layer
    return coord
