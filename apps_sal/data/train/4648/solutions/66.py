def automorphic(n):
    x = len(str(n))
    sq = str(n**2)
    return "Automorphic" if sq[-x:] == str(n) else "Not!!"
