def automorphic(n):
    end = int(str(n ** 2)[-len(str(n)):])
    return 'Automorphic' if end == n else 'Not!!'
