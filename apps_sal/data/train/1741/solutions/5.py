def five_by_2n(n):
    (a1, a2, a3, a4) = (1, 8, 95, 1183)
    for i in range(n):
        nxt = (15 * a4 - 32 * a3 + 15 * a2 - a1) % 12345787
        (a1, a2, a3, a4) = (a2, a3, a4, nxt)
    return a1
