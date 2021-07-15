DIGIT_CNTS = [1] + [(10**i - 10**(i-1)) * i for i in range(1, 20)]

def champernowneDigit(n):
    if not isinstance(n, int) or n is True or n <= 0:
        return float('nan')
    n -= 1
    for digits, cnt in enumerate(DIGIT_CNTS):
        if n < cnt:
            break
        n -= cnt
    start = int(10 ** (digits-1))
    q, r = divmod(n, digits) if digits > 1 else (n, 0)
    return int(str(start + q)[r])
