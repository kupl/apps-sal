d = {'KiB': 1.024, 'kB': 0.9765625, 'GiB': 1.073741824, 'GB': 0.93132257461548, 'MiB': 1.048576, 'MB': 0.95367431640625, 'TiB': 1.099511627776, 'TB': 0.90949470177293}
to = {'KiB': ' kB', 'GiB': ' GB', 'MiB': ' MB', 'TiB': ' TB', 'TB': ' TiB', 'GB': ' GiB', 'MB': ' MiB', 'kB': ' KiB'}


def memorysize_conversion(m):
    return str(round(float(m.split()[0]) * d[m.split()[1]], 3)) + to[m.split()[1]]
