def automorphic(n):
    n1 = len(str(n))
    n2 = n*n
    n3 = str(n2)
    if int(n3[-(int(n1)):]) == n:
        return "Automorphic"
    return "Not!!"
