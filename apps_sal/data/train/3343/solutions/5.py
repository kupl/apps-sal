kibi = ['KiB', 'MiB', 'GiB', 'TiB']
si = ['kB', 'MB', 'GB', 'TB']


def memorysize_conversion(size):
    val, unit = size.split()
    n = 'KMGT'.index(unit[0].upper())

    if unit in kibi:
        return '%s %s' % (round(float(val) * 1.024 ** (n + 1), 3), si[n])
    else:
        return '%s %s' % (round(float(val) / 1.024 ** (n + 1), 3), kibi[n])
