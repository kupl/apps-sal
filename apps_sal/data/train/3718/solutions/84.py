def divisors(n):
    list = []
    for i in range(1,500000):
        if n % i == 0:
            list.append(i)
    return len(list)
