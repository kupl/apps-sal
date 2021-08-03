DEFAULT = "There is no possible number that fulfills those requirements"


def valid(s): return len(set(s)) == len(s)


def next_numb(n):
    n += 3 - n % 3
    if not n & 1:
        n += 3
    return next((n for n in range(n, 9999999999, 6) if valid(str(n))), DEFAULT)
