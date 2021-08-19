def withdraw(n):
    n50 = 0
    (n20, r) = divmod(n, 20)
    if r == 10:
        n20 -= 2
        n50 += 1
    (n100, n20) = divmod(n20, 5)
    return [n100, n50, n20]
