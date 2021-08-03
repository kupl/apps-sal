def min_sum(arr):
    return rec(sorted(arr))


def rec(arr, n=0):
    return n if not arr else rec(arr, n + arr.pop(0) * arr.pop(-1))
