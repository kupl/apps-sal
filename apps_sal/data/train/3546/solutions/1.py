def validate_ean(code):
    (data, last) = (code[:12], int(code[12]))
    checksum = -sum((int(d) * 3 ** (i % 2) for (i, d) in enumerate(data))) % 10
    return last == checksum
