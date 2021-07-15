def digits(n):
    total = 1
    while n // 10 >= 1:
        n //= 10
        print(n)
        total += 1
    return total
