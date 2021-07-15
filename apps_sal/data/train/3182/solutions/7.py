def LDTA(n):
    if n in (1, 10, 100, 1000, 10000):
        return None
    digits = set("0123456789")
    k = 1
    while True:
        p = str(n**k)
        for digit in p:
            digits -= {digit}
            if len(digits) == 1:
                return int(digits.pop())
        k += 1
