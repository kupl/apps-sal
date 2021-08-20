def automorphic(n):
    return {0: 'Not!!', 1: 'Automorphic'}[str(n * n)[-len(str(n)):] == str(n)]
