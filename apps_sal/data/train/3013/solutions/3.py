def delete_digit(n):
    n = str(n)
    res = 0
    for i in range(len(n)):
        digit = int(n[0:i] + n[i + 1:])
        if digit > res:
            res = digit
    return res
