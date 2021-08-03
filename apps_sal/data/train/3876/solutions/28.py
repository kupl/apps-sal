def find(n):
    sum = 0
    for i in range(0, n + 1, 3):
        sum = sum + i
    for i in range(0, n + 1, 5):
        if i % 3 != 0:
            sum = sum + i
    return sum
