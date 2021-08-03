def shortest_arrang(n):
    a = n // 2
    b = a + 1

    while a:
        total = sum(range(a, b + 1))
        if total == n:
            return list(range(b, a - 1, -1))

        if total > n:
            b -= 1
            a = b - 1
        else:
            a -= 1
    else:
        return [-1]
