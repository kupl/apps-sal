def skrzat(base, number):
    s = 0xAAAAAAAA

    if base == 'b':
        i = int(number, 2)
        return f"From binary: {number} is {(s ^ i) - s}"
    elif base == 'd':
        return f"From decimal: {number} is {(number + s) ^ s:b}"
