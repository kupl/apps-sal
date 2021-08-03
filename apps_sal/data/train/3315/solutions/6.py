def strongest_even(n, m):
    n = n if n % 2 == 0 else n + 1
    m = m if m % 2 == 0 else m - 1

    x = 2

    while not x * 2 > m:
        x *= 2

    if x < n:
        i, s, a = m, n, x

        while i >= n:
            if i % a / 2 == 0:
                s = i
                i -= a
                a = x

            a = a / 2 if a / 2 > 1 else 2

        return s
    else:
        return x
