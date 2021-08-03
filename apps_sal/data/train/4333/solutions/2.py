def sort_number(a):
    a = sorted(a)
    m = a.pop(-1)
    return [[1] + a, a + [2]][m == 1]
