from itertools import permutations as perms


def is_pand(n):
    return len(set(list(str(n)))) == len(str(n))


def next_pan(n):
    while True:
        if is_pand(n):
            yield n
        n += 1


def get_sequence(n, k):
    if n < 1023456789:
        n = 1023456789
    elif n >= 9999999999:
        return []
    if not is_pand(n):
        n = next(next_pan(n))
    res = []
    for i in next_pan(n):
        res.append(i)
        if len(res) == k:
            break
    return res
