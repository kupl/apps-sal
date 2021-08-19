def automorphic(n):
    return 'Automorphic' if int(str(n * n - n)[-len(str(n)):]) == 0 else 'Not!!'
