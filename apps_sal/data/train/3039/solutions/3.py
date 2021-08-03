import itertools


def dig_sum(n):
    return sum([int(x) for x in str(n)])


def harshad_list(n):
    if n == 0:
        return []
    deci = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
    n -= 1
    while n != 0:
        temp = []
        for d in deci[-1]:
            e = 10 * d
            for tail in range(10):
                if (e + tail) % dig_sum(e + tail) == 0:
                    temp.append(e + tail)
        n -= 1
        deci.append(temp)
    return deci


pre_calc = list(itertools.chain.from_iterable(harshad_list(16)))


def rthn_between(a, b):
    res = []
    for i in pre_calc:
        if i >= a and i <= b:
            if i > 9:
                res.append(i)
    return res
