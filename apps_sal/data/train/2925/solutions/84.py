def multiply(n):
    count = 0
    if n < 0:
        num = -n
    else:
        num = n
    while num > 0:
        num = num // 10
        count += 1
    return (n * (5**count))
