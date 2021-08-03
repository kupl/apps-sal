def convert_num(number, base):
    if not isinstance(number, int):
        return "Invalid number input"
    if base == 'hex':
        return hex(number)
    elif base == 'bin':
        return bin(number)
    return "Invalid base input"
