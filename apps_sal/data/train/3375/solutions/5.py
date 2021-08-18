def trunc(n):
    return float(str(n)[:8])


def going(n):
    sum = 1
    fact = 1.0
    for i in range(1, n):
        fact = fact / (n - i + 1)
        sum += fact
    return trunc(sum)
