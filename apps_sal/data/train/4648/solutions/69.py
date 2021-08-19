def automorphic(n):
    return ['Not!!', 'Automorphic'][all((a == b for (a, b) in zip(str(n)[::-1], str(n ** 2)[::-1])))]
