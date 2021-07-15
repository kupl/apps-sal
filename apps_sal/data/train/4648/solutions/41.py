def automorphic(n):
    size = len(str(n))
    return "Automorphic" if str(n * n)[-size:] == str(n) else "Not!!"

