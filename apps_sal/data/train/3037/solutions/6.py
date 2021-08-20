from collections import Counter


def obtain_max_number(arr):
    return (lambda n: max(n) if len(arr) == len(n) else obtain_max_number(n))(sum([[2 * k] * (v // 2) + [k] * (v % 2) for (k, v) in Counter(arr).items()], []))
