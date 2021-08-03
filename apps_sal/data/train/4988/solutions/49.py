from scipy.integrate import quad as integrate


def square(n):
    return sum(set([round(value, 5) for value in (
        n**2,
        n * n,
        (lambda x: x**2)(n),
        (lambda x: x * x)(n),
        (lambda x: integrate(lambda a, b: b, min(0, n), max(0, n), args=n))(n)[0],
        sum(n for _ in range(int(n))) + n * (n - n // 1 + 0 if n >= 0 else 1)
    )]))
