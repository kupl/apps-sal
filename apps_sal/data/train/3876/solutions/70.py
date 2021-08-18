def find(n):
    if n < 3:
        return 0
    sum = 0
    for i in range(3, n + 1):
        if (i % 3 == 0) | (i % 5 == 0):
            sum += i
    return sum
