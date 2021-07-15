def solomons_quest(arr):
    level = 0
    ds = [1j, 1, -1j, -1]
    pos = 0
    for level_shift, direction, distance in arr:
        level += level_shift
        pos += (2**level) * (ds[direction] * distance)
    return [int(pos.real), int(pos.imag)]
