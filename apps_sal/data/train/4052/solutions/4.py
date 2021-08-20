import itertools


def get_num(arr):
    n = 1
    amount = 1
    div = []
    for i in arr:
        n = n * i
        if i not in div:
            amount = amount * (arr.count(i) + 1)
            div.append(i)
    lil_div = min(arr)
    big_div = n // lil_div
    return [n, amount - 1, lil_div, big_div]
