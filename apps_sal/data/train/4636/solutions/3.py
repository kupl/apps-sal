def tv_remote(word):
    (shift, kb) = (coords['↑'], 0)
    (moves, current) = (0, (0, 0))
    for char in word:
        (target, switch) = (coords[char.lower()], get_switch(kb, char))
        if switch:
            (moves, current, kb) = (moves + switch - 1 + distance(current, shift), shift, (kb + switch) % 3)
        (moves, current) = (moves + distance(current, target), target)
    return moves


kb1 = ('abcde123', 'fghij456', 'klmno789', 'pqrst.@0', 'uvwxyz_/', '↑ ')
kb3 = ('^~?!\'"()', '-:;+&%*=', '<>€£$¥¤\\', '[]{},.@§', '#¿¡\xa0\xa0\xa0_/')
coords = {c: (line.index(c), y) for kb in (kb1, kb3) for (y, line) in enumerate(kb) for c in line}


def get_switch(kb, char):
    target = 0 if char.islower() else 1 if char.isupper() else kb != 2 and kb if char.isdecimal() else 2 if char not in '.@_/↑ ' else kb
    return (target - kb) % 3


def distance(pos1, pos2):
    (d0, d1) = (abs(pos2[0] - pos1[0]), abs(pos2[1] - pos1[1]))
    return 1 + min(d0, 8 - d0) + min(d1, 6 - d1)
