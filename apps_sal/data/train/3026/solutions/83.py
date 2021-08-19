from itertools import permutations


def min_value(digits):
    b = []
    a = list(permutations(set(digits)))
    for x in a:
        x = [str(y) for y in x]
#         print(x)
        b.append(int(''.join(x)))
    return min(b)
