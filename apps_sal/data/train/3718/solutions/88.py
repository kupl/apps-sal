def divisors(n):
    temp = []
    for i in range(1, 600000):
        if n % i == 0:
            temp.append(i)
    return len(temp)
