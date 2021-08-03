def automorphic(n):
    n, s = str(n), str(n * n)
    return 'Automorphic' if n == s[len(n) * -1:] else 'Not!!'
