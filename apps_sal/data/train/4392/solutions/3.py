def find_lowest_int(k):
    (l, n) = (k + 1, 9)
    while digits(k * n) != digits(l * n):
        n += 9
    return n


def digits(n):
    return sorted(str(n))
