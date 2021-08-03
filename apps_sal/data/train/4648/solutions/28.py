def automorphic(n):
    s = str(n)
    l = len(s)
    return "Automorphic" if str(n**2)[-l:] == s else "Not!!"
