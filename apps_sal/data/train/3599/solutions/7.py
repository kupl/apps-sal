def less_than(n, k):
    return all((int(x) < k for x in str(n)))


def has_all(n, k):
    s = str(n)
    for i in range(10):
        if i < k and str(i) not in s:
            return False
        if i >= k and str(i) in s:
            return False
    return True


def f1(n, k):
    cn = n
    while not less_than(cn, k):
        cn += n
    return cn


def f2(n, k):
    cn = n
    while not has_all(cn, k):
        cn += n
    return cn


def find_f1_eq_f2(n, k):
    n += 1
    while f1(n, k) != f2(n, k):
        n += 1
    return n
