def automorphic(n):
    n2 = n * n
    return 'Automorphic' if str(n) == str(n2)[-len(str(n)):] else 'Not!!'
