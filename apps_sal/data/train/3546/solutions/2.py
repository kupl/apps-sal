def validate_ean(code):
    checksum = int(code[-1:])
    code = list(map(int, code[:-1]))
    odd = sum([code[i] for i in range(0, len(code), 2)])
    even = sum([code[i] * 3 for i in range(1, len(code), 2)])
    total = odd + even
    if total % 10 == 0:
        if checksum == 0:
            return True
        else:
            return False
    else:
        new_checksum = 10 - (total % 10)
        if new_checksum == checksum:
            return True
        else:
            return False
