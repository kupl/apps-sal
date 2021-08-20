def find_lowest_int(k1):
    (k2, n) = (k1 + 1, 1)

    def digits(n):
        return sorted(str(n))
    while digits(n * k1) != digits(n * k2):
        n += 1
    return n
