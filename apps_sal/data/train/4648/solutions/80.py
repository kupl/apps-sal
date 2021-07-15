def automorphic(n):
    i = n
    d = 1
    while i >= 1:
        d *= 10
        i /= 10
    if n == (n * n) % d:
            return "Automorphic"
    return "Not!!"
