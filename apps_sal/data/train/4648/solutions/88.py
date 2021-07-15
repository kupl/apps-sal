def automorphic(n):
    a = ([int(x) for x in str(n)])
    b = ([int(x) for x in str(n*n)])
    for i in range(1, len(a)+1):
        if a[len(a) - i] != b[len(b) - i]:
            return "Not!!"
    return "Automorphic"
