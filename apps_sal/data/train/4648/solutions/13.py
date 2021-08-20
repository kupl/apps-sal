def automorphic(n):
    return 'Automorphic' if n ** 2 % 10 ** len(str(n)) == n else 'Not!!'
