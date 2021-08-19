from collections import Counter


def fib(n):
    (v1, v2, v3) = (1, 1, 0)
    for rec in bin(n)[3:]:
        calc = v2 * v2
        (v1, v2, v3) = (v1 * v1 + calc, (v1 + v3) * v2, calc + v3 * v3)
        if rec == '1':
            (v1, v2, v3) = (v1 + v2, v1, v2)
    return v2


def fib_digits(n):
    return sorted(((v, int(k)) for (k, v) in Counter(str(fib(n))).items()), reverse=True)
