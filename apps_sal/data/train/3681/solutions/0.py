def convert_num(number, base):
    try:
        if base == 'hex':
            return hex(number)
        if base == 'bin':
            return bin(number)
    except:
        return 'Invalid number input'
    return 'Invalid base input'
