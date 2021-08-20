def find_min_num(d, n=1):
    while div_num(n) != d:
        n += 1
    return n


def div_num(n):
    s = n ** 0.5
    return sum((2 for k in range(1, int(s) + 1) if n % k == 0)) - (s % 1 == 0)
