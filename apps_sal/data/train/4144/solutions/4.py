def abundant(h):
    for n in range(h, 0, -1):
        s = sum((d + n // d for d in range(2, int(n ** 0.5) + 1) if not n % d)) - n ** 0.5 * (not n ** 0.5 % 1) + 1
        if s > n:
            return [[n], [s - n]]
