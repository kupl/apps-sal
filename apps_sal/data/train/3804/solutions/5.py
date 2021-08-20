def check(m):
    a = list(range(1, m + 1))
    b = a[::-1]
    c = 0
    for (x, y) in zip(a, b):
        c += x ** y
    return str(c)


lst = [1, 1] + [len(check(i)) for i in range(2, 1001)]


def min_length_num(num_dig, ord_max):
    arr = lst[:ord_max]
    if num_dig in arr:
        return [True, arr.index(num_dig) + 1]
    return [False, -1]
