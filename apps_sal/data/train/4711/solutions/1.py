def zeros(n):
    zeros = 0
    i = 5
    while n//i > 0:
        zeros += n//i
        i*=5
    return zeros
