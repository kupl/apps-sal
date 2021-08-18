from itertools import count


def gen():
    for x in count(0, 9):
        y = int(str(x)[::-1])
        if x != y and x % 10 and (x + y) % abs(x - y) == 0:
            yield x


numbers, result = gen(), []


def sum_dif_rev(n):
    while len(result) < n:
        result.append(next(numbers))
    return result[n - 1]
