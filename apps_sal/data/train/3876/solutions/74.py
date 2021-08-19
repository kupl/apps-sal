def find(n):
    # Code here
    sum = 0
    for i in range(n + 1):
        if i % 5 == 0:
            sum = sum + i
        elif i % 3 == 0:
            sum = sum + i

    return sum
