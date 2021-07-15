def automorphic(n):
    ls=n**2
    return 'Automorphic' if str(n)==str(n**2)[-len(str(n)):] else 'Not!!'

