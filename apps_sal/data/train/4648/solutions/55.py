def automorphic(n):
    l = len(str(n))
    m = 10**l
    return "Automorphic" if n * n % m == n else "Not!!"
