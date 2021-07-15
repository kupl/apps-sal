def automorphic(n):
    n2 = n**2
    if str(n2)[-len(str(n)):] == str(n):
        return 'Automorphic'
    else:
        return 'Not!!'
