from statistics import mean


def func(l):
    m = int(mean(l))
    return [m, (''.join('1' if m & 2 ** i else '0' for i in range(99, -1, -1)).lstrip('0')), f'{m:o}', f'{m:x}']
