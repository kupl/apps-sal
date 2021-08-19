from collections import deque


def group_cities(seq):
    result = []
    seq = sorted(set(seq))
    simples = [c.lower() for c in seq]
    skip = set()
    for (i, c1) in enumerate(simples):
        if i in skip:
            continue
        city_match = [i]
        skip.add(i)
        rolls = []
        roller = deque(c1)
        roller.rotate(1)
        while ''.join(roller) != c1:
            rolls.append(''.join(roller))
            roller.rotate(1)
        for roll in rolls:
            for (j, c2) in enumerate(simples[i + 1:], i + 1):
                if j in skip:
                    continue
                if c2 == roll:
                    skip.add(j)
                    city_match.append(j)
        result.append(sorted([seq[k] for k in city_match]))
    result.sort(key=lambda a: (-len(a), a[0]))
    return result
