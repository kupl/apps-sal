def automorphic(n):
    l = len(str(n))
    return 'Automorphic' if n * n % 10 ** l == n else 'Not!!'
