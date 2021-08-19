def squares_needed(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    i = 1
    cont = 1
    sum = 1
    while sum < n:
        i *= 2
        sum += i
        cont += 1
    return cont
