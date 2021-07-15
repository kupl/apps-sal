grid = ["abcde123", "fghij456", "klmno789", "pqrst.@0", "uvwxyz_/"]

def tv_remote(word):
    steps = 0
    pos = (0, 0)
    for c in word:
        index = next((grid.index(x), x.index(c)) for x in grid if c in x)
        steps += abs(index[0] - pos[0]) + abs(index[1] - pos[1]) + 1
        pos = index
    return steps
