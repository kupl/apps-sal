def dig_pow(n, p):
    sum = 0
    for c in str(n):
        sum += int(c) ** p
        p += 1
    if sum % n == 0:
        return sum / n
    else:
        return -1
