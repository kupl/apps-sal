def divisors(n):

    def gen_divisors():
        y = 1
        while y <= n:
            if n % y == 0:
                yield y
            y += 1
    return len(list(gen_divisors()))
