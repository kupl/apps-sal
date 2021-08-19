keyboard = 'abcde123fghij456klmno789pqrst.@0uvwxyz_/'
MAP = {c: (i // 8, i % 8) for (i, c) in enumerate(keyboard)}


def tv_remote(word):
    cur = (0, 0)
    steps = 0
    for c in word:
        steps += 1 + abs(cur[0] - MAP.get(c)[0]) + abs(cur[1] - MAP.get(c)[1])
        cur = MAP.get(c)
    return steps
