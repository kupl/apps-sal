def gap(g, m, n):
    def isprime(i):
        if i <= 3:
            return i > 1
        elif i % 2 == 0 or i % 3 == 0:
            return False
        x = 5
        while x * x <= n:
            if i % x == 0 or i % (x + 2) == 0:
                return False
            x += 6
        return True

    lp = 2
    for j in range(m, n + 1):
        if isprime(j):
            if j - lp == g:
                return [lp, j]
            lp = j
    return None
