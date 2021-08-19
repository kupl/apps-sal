def tv_remote(word):
    (caps, cases, shift) = (coords['↑'], (str.isupper, str.islower), 0)
    (moves, current) = (0, (0, 0))
    for char in word:
        target = coords[char.lower()]
        if cases[shift](char):
            (moves, current, shift) = (moves + distance(current, caps), caps, 1 - shift)
        (moves, current) = (moves + distance(current, target), target)
    return moves


keyboard = ('abcde123', 'fghij456', 'klmno789', 'pqrst.@0', 'uvwxyz_/', '↑ ')
coords = {char: (line.index(char), y) for (y, line) in enumerate(keyboard) for char in line}


def distance(pos1, pos2):
    (d0, d1) = (abs(pos2[0] - pos1[0]), abs(pos2[1] - pos1[1]))
    return 1 + min(d0, 8 - d0) + min(d1, 6 - d1)
