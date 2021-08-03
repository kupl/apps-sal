def increasing_numbers(d):
    s = 1
    for i in range(1, 10):
        s = s * (i + d) // i
    return s
