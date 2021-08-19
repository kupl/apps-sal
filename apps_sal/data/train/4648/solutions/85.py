def automorphic(n):
    if str(n ** 2)[-len(str(n)):] == str(n):
        return 'Automorphic'
    return 'Not!!'
