def automorphic(n):
    return 'Automorphic' if str(n) in str(n ** 2)[-len(str(n)):] else 'Not!!'
