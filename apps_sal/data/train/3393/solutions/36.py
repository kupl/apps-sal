def list_squared(m, n):
    a = []
    b = []
    for i in range(m, n):
        sum = 0
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                sum += j ** 2
                if i / j != j:
                    sum += int(i / j) ** 2
        if (sum ** 0.5).is_integer():
            a.append(i)
            b.append(sum)
    return [list(i) for i in zip(a, b)]
