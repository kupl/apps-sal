deck = set('123456789')


def group(tiles, start, pair=None):
    if len(tiles) == 1:
        return [tiles]

    if len(tiles) == 2:
        if tiles[0] == tiles[1]:
            return [pair, tiles[0]]
        else:
            a, b = ord(max(tiles[0], tiles[1])), ord(min(tiles[0], tiles[1]))
            if a - b == 1:
                r = []
                if chr(a + 1) in deck:
                    r.append(chr(a + 1))
                if chr(b - 1) in deck:
                    r.append(chr(b - 1))
                return r
            elif a - b == 2:
                return [chr(b + 1)]
        return []

    tiles_set = set(tiles)
    ret = []
    for tile in tiles_set:
        if tile < start:
            continue

        if len(tiles) % 3 == 1 and tiles.count(tile) > 1:
            ret.extend(group(tiles.replace(tile, '', 2), tile, tile))
        if tiles.count(tile) > 2:
            ret.extend(group(tiles.replace(tile, '', 3), tile, pair))

        a, b = chr(ord(tile) + 1), chr(ord(tile) + 2)
        if a in tiles_set and b in tiles_set:
            ret.extend(group(tiles.replace(tile, '', 1)
                             .replace(a, '', 1).replace(b, '', 1), tile, pair))
    return ret


def solution(tiles):
    return ''.join(sorted([x for x in set(group(tiles, tiles[0])) if tiles.count(x) < 4]))

