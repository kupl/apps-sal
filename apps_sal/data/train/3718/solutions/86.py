def divisors(n):
    i = 1
    lt = []
    while i <= n:
        if (n % i == 0):
            lt.append(i)
        i = i + 1
    return len(lt)
