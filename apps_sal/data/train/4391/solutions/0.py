def yellow_be_gone(s):
    d = {'gold': 'ForestGreen', 'khaki': 'LimeGreen', 'lemonchiffon': 'PaleGreen', 'lightgoldenrodyellow': 'SpringGreen',
         'lightyellow': 'MintCream', 'palegoldenrod': 'LightGreen', 'yellow': 'Lime'}

    if s[0] == '
    R, G, B = s[1:3], s[3:5], s[5:]
    if B < G and B < R:
        R, B, G = sorted([R, G, B])
        s = '

    return d.get(s.lower(), s)
