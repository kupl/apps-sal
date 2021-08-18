import re
h = {
    'gold': 'ForestGreen',
    'khaki': 'LimeGreen',
    'lemonchiffon': 'PaleGreen',
    'lightgoldenrodyellow': 'SpringGreen',
    'lightyellow': 'MintCream',
    'palegoldenrod': 'LightGreen',
    'yellow': 'Lime',
}


def yellow_be_gone(c):
    n = c.lower()
    if n in h:
        return h[n]

    m = re.match(r'
    if m:
        r, g, b=list(m.groups())
        l=sorted([r, g, b])
        if(r > b and g > b):
            return'
    return c
