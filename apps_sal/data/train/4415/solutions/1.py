from math import factorial


def proc_arr(arr):
    arr = ''.join(sorted(arr))
    comb = factorial(len(arr))
    same = eval('*'.join(map(str, [factorial(arr.count(n)) for n in '0123456879'])))

    return [comb / same, int(arr), int(arr[::-1])]
