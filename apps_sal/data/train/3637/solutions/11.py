from functools import reduce


def num_primorial(n):
    from operator import mul
    from functools import reduce
    lst = []
    i = 2
    while len(lst) != n:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
        i += 1
    return reduce(mul, lst)
