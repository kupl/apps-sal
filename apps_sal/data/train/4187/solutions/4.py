def solomons_quest(arr):
    south_north = 0
    east_west = 0
    layer = 0
    for el in arr:
        layer += el[0]
        if el[1] == 0:
            south_north += el[2] * 2 ** layer
        elif el[1] == 2:
            south_north -= el[2] * 2 ** layer
        elif el[1] == 1:
            east_west += el[2] * 2 ** layer
        elif el[1] == 3:
            east_west -= el[2] * 2 ** layer
    return [east_west, south_north]
