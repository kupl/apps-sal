def split(string):
    return [char for char in string]


layout = [split("abcde123"),
          split("fghij456"),
          split("klmno789"),
          split("pqrst.@0"),
          split("uvwxyz_/")]

position = dict((j, (x, y)) for x, i in enumerate(layout) for y, j in enumerate(i))


def tv_remote(word):
    presses = 0
    current = 'a'
    for i, char in enumerate(word):
        target = char
        distance = abs(position[current][0] - position[target][0]) + abs(position[current][1] - position[target][1])
        presses += distance + 1
        current = char
    return presses
