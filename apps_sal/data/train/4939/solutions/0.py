def coffee_limits(year, month, day):
    h = int(f'{year:04}{month:02}{day:02}')
    return [limit(h, 51966), limit(h, 912559)]


def limit(h, c):
    for i in range(1, 5000):
        h += c
        if 'DEAD' in f'{h:X}':
            return i
    return 0
