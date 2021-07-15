from itertools import permutations

square = lambda p: not int(''.join(p))**0.5%1
count = lambda num: sum(map(square, set(permutations(str(num)))))

def sort_by_perfsq(arr):
    return sorted(arr, key=lambda x: (-count(x), x))
