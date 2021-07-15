def zeros(n):
    sum = 0
    for i in range(1, 30):
        sum += n//(5**i)
    return sum
