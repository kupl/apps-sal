def find(n):
    n = n + 1
    sum = 0
    for x in range(n):
        if x % 3 == 0 or x % 5 == 0:
            sum += x
    return sum
