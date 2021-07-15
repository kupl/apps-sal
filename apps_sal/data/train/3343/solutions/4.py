from decimal import Decimal, ROUND_HALF_UP

units = 'KMGT'
q = Decimal('0.001')

def memorysize_conversion(memorysize):
    n, unit = memorysize.split()
    n = Decimal(n)
    i = units.find(unit[0].upper()) + 1
    if unit[1] == 'i':
        n *= 1024 ** i
        n /= 1000 ** i
        new_unit = ['kB', 'MB', 'GB', 'TB'][i-1]
    else:
        n *= 1000 ** i
        n /= 1024 ** i
        new_unit = ['KiB', 'MiB', 'GiB', 'TiB'][i-1]
    new_value = format(n.quantize(n, rounding=ROUND_HALF_UP), '.3f').rstrip('0.')
    return f'{new_value} {new_unit}'
