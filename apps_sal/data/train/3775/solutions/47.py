def digits(n):
    # your code here
    i = 0
    while n > 0:
        i += 1
        n = n // 10
    return i
