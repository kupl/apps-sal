def automorphic(n):
    m = str(n)
    b = str(n**2)
    return "Automorphic" if b[slice(len(b) - len(m), len(b), 1)] == m else "Not!!"
