CONV = {'KiB': 'kB', 'MiB': 'MB', 'GiB': 'GB', 'TiB': 'TB',
        'kB': 'KiB', 'MB': 'MiB', 'GB': 'GiB', 'TB': 'TiB'}

def memorysize_conversion(size):
    val, unit = size.split()
    val = float(val)
    p = 'KMGT'.index(unit[0].upper()) + 1
    
    r = 1.024 if 'i' in unit else 1 / 1.024
    
    return '%s %s' % (round(val * r ** p, 3), CONV[unit])
