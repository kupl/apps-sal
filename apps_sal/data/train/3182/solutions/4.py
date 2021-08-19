def LDTA(n):
    digits = []
    num = 1
    pow = 1
    while num < n ** pow and pow < 20:
        num *= n
        pow += 1
        if len(digits) == 10:
            return digits[-1]
        else:
            for d in str(num):
                if int(d) not in digits:
                    digits.append(int(d))
    return None
