def automorphic(n):
    if n == int(str(n ** 2)[-len(str(n)):]):
        return 'Automorphic'
    else:
        return 'Not!!'
