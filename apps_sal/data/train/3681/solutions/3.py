def convert_num(number, base):
    if base not in ('hex', 'bin'):
        return 'Invalid base input'
    try:
        return hex(number) if base == 'hex' else bin(number)
    except:
        return 'Invalid number input'
