import itertools


def twodigcombs(n):
    ls = []
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for (x, y) in itertools.combinations_with_replacement(digits, 2):
        if x + y == n:
            ls.append([x, y])
    return sorted(ls)


def generate_number(squad, n):
    print((squad, n))
    if n not in squad:
        return n
    for [a, b] in twodigcombs(n):
        x = a * 10 + b
        if x not in squad:
            return x
