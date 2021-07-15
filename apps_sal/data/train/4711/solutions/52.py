def zeros(n):
    i = 5
    count_5 = 0
    while n//i >= 1:
        count_5 += n//i
        i *= 5
    return count_5

