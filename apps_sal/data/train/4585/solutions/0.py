def find(a, b, n):
    strng = str(a) + str(b)
    if n > 20:
        n = n % 20 + 20
    while len(strng) <= n:
        next_ch = int(strng[-1]) + int(strng[-2])
        strng = strng + str(next_ch)
    return int(strng[n])
