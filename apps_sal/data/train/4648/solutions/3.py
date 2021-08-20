def automorphic(n):
    return 'Automorphic' if n == n ** 2 % 10 ** len(str(n)) else 'Not!!'
