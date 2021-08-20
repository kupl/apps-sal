def zeros(n):
    i = 5
    count = 0
    while i < n:
        count += n // i
        i = i * 5
    return count
