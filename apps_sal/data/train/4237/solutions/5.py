def to12hourtime(s):
    h, m = divmod(int(s), 100)
    p, h = divmod(h, 12)
    return '{}:{:02} {}m'.format(h or 12, m, 'p' if p else 'a')
