import re


def dec_to_base(num, base):
    res = ''
    while num > 0:
        dig = int(num % base)
        if dig < 10:
            rem = num % base
        else:
            rem = 'x'
        res = str(rem) + res
        num //= base
    return res


def fouriest(i):
    (lst, lst2) = ([], [])
    for j in range(2, 500):
        n = str(dec_to_base(i, j))
        lst.append(n)
        lst2.append(n.count('4'))
    ind = lst2.index(max(lst2)) + 2
    return f'{i} is the fouriest ({lst[ind - 2]}) in base {ind}'
