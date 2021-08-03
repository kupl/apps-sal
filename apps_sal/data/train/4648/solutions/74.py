def automorphic(n):
    X = (n**2) - n
    return "Automorphic" if X % (10**len(str(n))) == 0 else "Not!!"
