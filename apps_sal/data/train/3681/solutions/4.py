def convert_num(number, base):
    try:
        if base == 'hex':
            return hex(number)
        elif base == 'bin':
            return bin(number)
        else:
            return 'Invalid base input'
    except:
        return 'Invalid number input'
