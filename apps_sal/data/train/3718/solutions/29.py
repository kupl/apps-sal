def divisors(n):
    L = []
    for i in range(1,n+1):
        if n//i == n/i:
            L.append(i)
    return len(L)
