def trotter(n):
    if n==0: return "INSOMNIA"
    seen, k = set(str(n)), 1
    while (not set("1234567890").issubset(seen)):
        k += 1
        seen.update(str(k*n))
    return n*k
