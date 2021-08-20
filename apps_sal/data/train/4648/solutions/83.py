def automorphic(n):
    return ('Automorphic', 'Not!!')[n != int(str(n * n)[-len(str(n)):])]
