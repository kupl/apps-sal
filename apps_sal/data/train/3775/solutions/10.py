def digits(n):
    if n == 0:
        return 1
    else:
        count = 0
        while n:
            count += 1
            n //= 10
        return count
