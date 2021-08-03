from collections import Counter


def next_numb(val):
    if val >= 9876543210:
        return "There is no possible number that fulfills those requirements"
    x = val + 1
    if x % 3 != 0:
        x += (3 - x % 3)
    if x % 2 == 0:
        x += 3
    c = Counter(str(x))
    while max(c.values()) > 1:
        x += 6
        c = Counter(str(x))
    return x
