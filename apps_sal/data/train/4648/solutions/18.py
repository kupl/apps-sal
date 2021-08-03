def automorphic(n):
    l = len(str(n))
    return 'Automorphic' if str(n) == str(n**2)[-l:] else 'Not!!'
