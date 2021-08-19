def convergents_of_e(n):
    (a0, a1, i) = (1, 2, 2)
    while i <= n:
        f = 1 if i % 3 else 2 * i // 3
        a = a0 + a1 * f
        (a0, a1) = (a1, a)
        i += 1
    return sum(map(int, str(a1)))
