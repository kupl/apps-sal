def check(n):
    r, l = 0, 0
    while n:
        n, v = divmod(n, 10)
        x = 0
        for i in range(l):
            x += 10**i * 2**(l - i - 1)
        r += r + v * x + v * 10**l
        l += 1
    return r


def next_higher(start_value, k):
    for i in range(start_value + 1, start_value + 30000):
        if check(i * k) - i - i * k == 0:
            return i
