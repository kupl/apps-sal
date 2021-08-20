def automorphic(n):
    if str(n * n)[-len(str(n)):] == str(n):
        return 'Automorphic'
    return 'Not!!'
