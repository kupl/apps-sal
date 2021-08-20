def validate_ean(code):
    """Return True if code is a valid EAN-13 code (else False)"""
    check_digit = int(code[-1])
    code = list(map(int, code[:-1]))
    totals = sum([digit * 3 if pos % 2 == 0 else digit for (pos, digit) in enumerate(code, 1)])
    if totals % 10 == 0:
        checksum = 0
    else:
        checksum = 10 - totals % 10
    return check_digit == checksum
