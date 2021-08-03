from itertools import combinations as comb


def numeric_palindrome(*args):
    args = [item for item in args if item > 0]
    if len(args) < 2:
        return 0
    if 1 in args:
        args = [item for item in args if item > 1] + [1]
    if len(args) == 1:
        return max_pal(list(str(args[0])))
    maxval = -1
    for i in range(2, len(args) + 1):
        base = comb(args, i)
        for combo in base:
            prod = 1
            for item in combo:
                prod *= item
            maxval = max(maxval, max_pal(list(str(prod))))
    return maxval


def max_pal(array):
    even = sorted([n * (array.count(n) / 2) for n in set(array) if array.count(n) > 1])
    odd = [n for n in set(array) if array.count(n) % 2 == 1]
    odd = [""] if len(odd) == 0 else odd
    if len(even) == 1 and even[0][0] == '0':
        even = [""]
    return int("".join(even[::-1] + [max(odd)] + even))
