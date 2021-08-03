def to12hourtime(timestring):
    h = int(timestring[:2])
    return '{}:{} {}m'.format(h % 12 or 12, timestring[2:], 'ap'[h > 11])
