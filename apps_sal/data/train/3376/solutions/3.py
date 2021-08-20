def square_free_part(n):
    if type(n) == int and n > 0:
        part = 1
        for p in range(2, int(n ** 0.5) + 1):
            if not n % p:
                part *= p
                while not n % p:
                    n //= p
        return part * n
