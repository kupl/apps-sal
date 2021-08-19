from itertools import combinations_with_replacement as c


def find(arr, n):
    return sum((sum(xs) == n for i in range(len(arr)) for xs in c(arr, i + 1)))
