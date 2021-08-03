def depth(arr, n):
    res = []
    for i in arr:
        if isinstance(i, int):
            res.append((i, n))
        else:
            res += depth(i, n + 1)
    return res


def sum_nested_numbers(arr):
    return sum(n**i for (n, i) in depth(arr, 1))
