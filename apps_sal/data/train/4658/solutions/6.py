def max_product(lst, n):
    lst = sorted(lst)[::-1]
    for _ in range(n - 1):
        rec(lst)
    return lst[0]


def rec(arr):
    arr[0] = arr.pop(0) * arr[0]
    return arr
