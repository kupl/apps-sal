def divs(n):
    s = 1
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            s += i
            s += n // i
    return s


def deficiently_abundant_amicable_numbers(n1, n2):
    (d1, d2) = map(divs, (n1, n2))

    def f(x, y):
        return 'perfect' if x == y else 'abundant' if x > y else 'deficient'
    return f"{f(d1, n1)} {f(d2, n2)} {('amicable' if d1 == n2 and d2 == n1 and (n1 != n2) else 'not amicable')}"
