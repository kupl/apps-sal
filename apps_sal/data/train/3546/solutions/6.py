def validate_ean(code):
    sum1 = sum(map(int, code[0:-1:2]))
    sum2 = sum(map(lambda x: x*3, map(int, code[1:-1:2])))
    checksum = 10 - ((sum1 + sum2) % 10)
    checksum = 0 if checksum == 10 else checksum
    return int(code[-1]) == checksum
