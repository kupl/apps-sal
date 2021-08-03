def abundant(h):
    for n in range(h, 0, -1):
        s = sum(i for i in range(1, n) if n % i == 0)
        if s > h:
            return [[n], [s - n]]
