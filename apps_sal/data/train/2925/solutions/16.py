def multiply(n):
    i = 10
    j = 1
    while True:
        if abs(n) < i:
            return n * 5 ** j
        else:
            i *= 10
            j += 1
