def champernowneDigit(n):
    if not isinstance(n, int) or isinstance(n, bool) or n <= 0:
        return float('nan')
    elif n <= 10:
        return n - 1
    nr_digits = 1
    mag_len = 10
    while n > mag_len:
        n -= mag_len
        nr_digits += 1
        mag_len = nr_digits * (10**nr_digits - 10**(nr_digits - 1))
        print(n, nr_digits, mag_len)
    quoitent, reminder = divmod(n - 1, nr_digits)
    print(quoitent, reminder)
    return int(str(quoitent + 10**(nr_digits - 1))[reminder])
