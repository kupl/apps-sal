def validate_ean(code):
    '''Return True if code is a valid EAN-13 code (else False)'''

    # separate single-digit checksum from code
    check_digit = int(code[-1])
    # convert 12-digit string to list of int
    code = list(map(int, code[:-1]))
    # multiply digits at even positions with 3
    totals = sum([digit * 3 if pos % 2 == 0 else digit for pos, digit in enumerate(code, 1)])

    if totals % 10 == 0:
        checksum = 0
    else:
        checksum = 10 - (totals % 10)
    return check_digit == checksum
