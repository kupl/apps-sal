def sum_digits(a):
    n = int(a)
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r

def order_weight(strng):
    strng_sorted = sorted(strng.split(), key = str.lower)
    return ' '.join(sorted(strng_sorted, key = sum_digits))
