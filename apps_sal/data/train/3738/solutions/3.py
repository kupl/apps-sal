fib = {3: 0, 4: 1, 5: 1}
for i in range(6, 31):
    fib[i] = fib[i - 2] + fib[i - 1]


def coefficients(n):
    y, z = 2, 0  # coefficients for number of passengers at station 3
    for i in range(4, n):
        y += fib[i - 1]
        z += fib[i]
    return y, z


def calc(k, n, m, x):
    y, z = coefficients(n)
    station2 = (m - y * k) // z
    y, z = coefficients(x + 1)
    return y * k + z * station2
