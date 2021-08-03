def digits_less_than(n, k):
    for i in str(n):
        if int(i) >= k:
            return False
    return True


def all_digits_less_than(n, d):
    for i in d:
        if i not in str(n):
            return False
    return True


def find_f1_eq_f2(n, k):
    d = '012'
    for i in range(3, k):
        d += str(i)
    m = 0
    i = 0
    while not all_digits_less_than((m + n) * i, d):
        m += 1
        i = 1
        while not digits_less_than((m + n) * i, k):
            i += 1
    return m + n
