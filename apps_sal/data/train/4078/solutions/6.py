from collections import Counter


def first_n_smallest(arr, n):

    def f():
        xs = Counter(sorted(arr)[:n])
        for x in arr:
            if xs[x]:
                xs[x] -= 1
                yield x
    return list(f())
