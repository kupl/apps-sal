def automorphic(n):
    return('Not!!', 'Automorphic')[str(n**2)[-len(str(n)):] == str(n)]
