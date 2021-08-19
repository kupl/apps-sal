def insert_dash(num):
    digits = [d for d in str(num)]
    for i in range(len(digits) - 1):
        if int(digits[i]) % 2 and int(digits[i + 1]) % 2:
            digits[i] = digits[i] + '-'
    return ''.join(digits)
