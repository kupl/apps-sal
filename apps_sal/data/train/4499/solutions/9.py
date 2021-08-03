def e_coeffs(n):
    def gen():
        i = 1
        while True:
            yield 1
            yield 2 * i
            i += 1
            yield 1
    x = gen()
    return [next(x) for _ in range(n)]


def convergents_of_e(n):
    if n <= 1:
        return 2
    xs = e_coeffs(n - 1)
    xs.reverse()
    p, q = 1, xs[0]
    for x in xs[1:]:
        p, q = q, x * q + p
    return sum(int(x) for x in str(2 * q + p))
