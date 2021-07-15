def validate_ean(code):
    sum_odd = sum(int(x) for x in code[:-1:2])
    sum_even = sum(int(x) * 3 for x in code[1::2])
    checksum = (sum_odd + sum_even) % 10
    if checksum:
        return (10 - checksum) == int(code[-1])
    else:
        return checksum == int(code[-1])
