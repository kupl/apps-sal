def reverse_number(n):
    if n == 0:
        return 0
    elif n < 0:
        ok = True
        n = -n
    else:
        ok = False
    while n % 10 == 0:
        n = n / 10
    aux = str(int(n))[::-1]
    if ok:
        return -int(aux)
    return int(aux)
