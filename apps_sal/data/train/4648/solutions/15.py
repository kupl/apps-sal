def automorphic(n):
    return ('Automorphic', 'Not!!')[(n**2 - n) % (10**(len(str(n)))) and 1]
