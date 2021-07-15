COLORS = {
    'gold': 'ForestGreen', 'khaki': 'LimeGreen', 'lemonchiffon': 'PaleGreen',
    'lightgoldenrodyellow': 'SpringGreen', 'lightyellow': 'MintCream',
    'palegoldenrod': 'LightGreen', 'yellow': 'Lime',
}

def yellow_be_gone(color):
    if color.startswith('#'):
        r, g, b = color[1:3], color[3:5], color[5:]
        if r > b < g:
            return '#{}{}{}'.format(b, max(r, g), min(r, g))
    return COLORS.get(color.lower(), color)
