def divisors(n):
    x = 1
    y = []
    while x < n:
        if n % x == 0:
            y.append(x)
        x +=1
    return len(y) + 1
