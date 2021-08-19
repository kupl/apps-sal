from functools import reduce


def get_factors(m):
    (li, j) = ([], 2)
    while j * j <= m:
        if m % j:
            j += 1
            continue
        m //= j
        li.append(j)
    return li + ([m] if m > 1 else [])


def divide(arr, cache):
    store = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            m = arr[:i] + arr[i + 1:j] + [arr[i] * arr[j]] + arr[j + 1:]
            tp = tuple(sorted(m))
            if m != arr and len(m) > 1 and (tp not in cache):
                cache.add(tp)
                store.extend([tp] + divide(m, cache))
    return store


def eq_dice(arr):
    (m, arr) = (reduce(lambda x, y: x * y, arr), tuple(sorted(arr)))
    return sum((1 for i in set(divide(get_factors(m), set())) if i != arr and all((2 < k < 21 for k in i))))
