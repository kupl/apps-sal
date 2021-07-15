def divisors(n):
    x = []
    for i in range(1,500001):
        if n % i == 0:
            x.append(i)
        else:
            continue
    return len(x)

