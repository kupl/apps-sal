from math import log


def decompose(a):
    (li, i) = ([], 2)
    while i ** 2 <= a:
        li.append(int(log(a, i)))
        a -= i ** li[-1]
        i += 1
    return [li] + [a]
