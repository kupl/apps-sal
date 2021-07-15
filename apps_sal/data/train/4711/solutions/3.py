def zeros(n):
    count = 0
    while n:
        n = n // 5
        count += n
    return count
