# lazy backtrack attempt

def validate(tiles, used_pair=False):
    tiles = sorted(tiles)
    if not tiles:
        return True

    current_tile = tiles.pop(0)
    if tiles.count(current_tile) > 1:
        tiles.remove(current_tile)
        tiles.remove(current_tile)
        ok = validate(tiles, used_pair)
        if ok:
            return True
        tiles.append(current_tile)
        tiles.append(current_tile)
        tiles = list(sorted(tiles))

    if tiles.count(current_tile + 1) > 0 and tiles.count(current_tile + 2) > 0:
        tiles.remove(current_tile + 1)
        tiles.remove(current_tile + 2)
        ok = validate(tiles, used_pair)
        if ok:
            return True
        tiles.append(current_tile + 1)
        tiles.append(current_tile + 2)
        tiles = list(sorted(tiles))

    if not used_pair and tiles.count(current_tile) > 0:
        tiles.remove(current_tile)
        ok = validate(tiles, True)
        if ok:
            return True
        tiles.append(current_tile)
        tiles = list(sorted(tiles))
    tiles.append(current_tile)
    return False


def solution(tiles):
    result = ''
    for i in range(1, 10):
        if tiles.count(str(i)) > 3:
            continue
        tiles_with_new_tile = [int(n) for n in sorted(tiles + str(i))]
        if validate(tiles_with_new_tile):
            result += str(i)
    return result
