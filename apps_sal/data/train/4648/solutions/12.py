def automorphic(n):
    s = str(n)
    t = str(n * n)
    return "Automorphic" if t[-len(s):] == s else "Not!!"
