def automorphic(n):
    if str(n ** 2)[-len(str(n)):] == str(n)[-len(str(n)):]:
        return 'Automorphic'
    else:
        return 'Not!!'
