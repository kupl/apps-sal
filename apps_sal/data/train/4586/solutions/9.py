def tv_remote(word):
    return len(word) + sum(distance(coords[a], coords[b]) for a, b in zip(f"a{word}", word))


keyboard = ("abcde123", "fghij456", "klmno789", "pqrst.@0", "uvwxyz_/")
coords = {char: (line.index(char), y) for y, line in enumerate(keyboard) for char in line}


def distance(pos1, pos2):
    return abs(pos2[0] - pos1[0]) + abs(pos2[1] - pos1[1])
