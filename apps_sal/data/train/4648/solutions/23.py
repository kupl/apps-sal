def automorphic(n):
    print(n)
    if str(n ** 2)[-len(str(n)):] == str(n):
        return 'Automorphic'
    return 'Not!!'
