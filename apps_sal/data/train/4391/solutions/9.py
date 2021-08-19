def yellow_be_gone(s):
    d = {'gold': 'ForestGreen', 'khaki': 'LimeGreen', 'lemonchiffon': 'PaleGreen', 'lightgoldenrodyellow': 'SpringGreen', 'lightyellow': 'MintCream', 'palegoldenrod': 'LightGreen', 'yellow': 'Lime'}
    if s.lower() in d:
        return d.get(s.lower())
    if not s.startswith('#'):
        return s
    flag = any(i.isupper() for i in s)
    r, g, b = map(lambda x: int(x, 16), (s[1:3], s[3:5], s[5:8]))
    if r > b and g > b:
        x, y, z = sorted((r, g, b))
        r, g, b = x, z, y
    c = '#' + ''.join(format(i, '02x') for i in (r, g, b))
    return c.upper() if flag else c
