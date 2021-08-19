def totient(n):
    try:
        assert isinstance(n, int) and n > 0
        phi = n
        if not n % 2:
            phi -= phi // 2
            while not n % 2:
                n //= 2
        for p in range(3, int(n ** 0.5) + 1, 2):
            if not n % p:
                phi -= phi // p
                while not n % p:
                    n //= p
        if n > 1:
            phi -= phi // n
        return phi
    except:
        return 0
