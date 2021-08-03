def automorphic(n):
    pow = 10 ** len(str(n))
    return 'Automorphic' if n == n * n % pow else 'Not!!'
