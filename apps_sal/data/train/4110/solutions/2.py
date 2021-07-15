from math import ceil


def matrixfy(stg):
    if not stg:
        return "name must be at least one letter"
    side = ceil(len(stg)**0.5)
    area = side**2
    chars = list(stg.ljust(area, "."))
    return [chars[i:i+side] for i in range(0, area, side)]

