from itertools import permutations


def square(p): return not int(''.join(p))**0.5 % 1
def count(num): return sum(map(square, set(permutations(str(num)))))


def sort_by_perfsq(arr):
    return sorted(arr, key=lambda x: (-count(x), x))
