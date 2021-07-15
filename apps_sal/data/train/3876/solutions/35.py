def find(n):
    sum = 0
    for a in range (1, n+1):
        if a%3 == 0 or a%5 == 0:
            sum = sum + a
    return sum
