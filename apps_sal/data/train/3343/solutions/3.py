(v1, v2) = (1000 / 1024, 1024 / 1000)
D1 = {'kB': v1, 'MB': v1 ** 2, 'GB': v1 ** 3, 'TB': v1 ** 4, 'KiB': v2, 'MiB': v2 ** 2, 'GiB': v2 ** 3, 'TiB': v2 ** 4}
D2 = {'kB': 'KiB', 'MB': 'MiB', 'GB': 'GiB', 'TB': 'TiB', 'KiB': 'kB', 'MiB': 'MB', 'GiB': 'GB', 'TiB': 'TB'}


def memorysize_conversion(memorysize):
    (x, y) = memorysize.split()
    return f'{round(float(x) * D1[y], 3)} {D2[y]}'
