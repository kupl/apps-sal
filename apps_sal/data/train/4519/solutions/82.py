from itertools import permutations


def max_number(n):
    n = str(n)
    l = []
    l = list(permutations(n))
    max = 0
    l2 = []
    for perm in l:
        l2.append(''.join(perm))
    for i in l2:
        if max < int(i):
            max = int(i)
    return max
