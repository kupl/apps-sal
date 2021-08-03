def totient(n):
    try:
        if n <= 0 or type(n).__name__ == str or n == None:
            return 0
        result = n
        p = 2
        while p * p <= n:
            if n % p == 0:
                while n % p == 0:
                    n = n // p
                result = result * (1 - (1 / float(p)))
            p = p + 1

        if (n > 1):
            result = result * (1 - (1 / float(n)))

        return int(result)
    except Exception:
        return 0
