from itertools import count


def find_f1_eq_f2(n, k):
    for x in count(n + 1):
        for y in count(x, x):
            if all(map(lambda c: int(c) < k, str(y))):
                if len(set(str(y))) == k:
                    return x
                else:
                    break
