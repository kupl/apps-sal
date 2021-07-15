def hotpo(n, count = 0):
    if n == 1:
        return count
    n = n//2 if n % 2 == 0 else 3*n + 1
    count += 1
    return hotpo(n, count)
