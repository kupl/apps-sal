def yellow_be_gone(color_name_or_code):
    d = {
        'gold': 'ForestGreen',
        'khaki': 'LimeGreen',
        'lemonchiffon': 'PaleGreen',
        'lightgoldenrodyellow': 'SpringGreen',
        'lightyellow': 'MintCream',
        'palegoldenrod': 'LightGreen',
        'yellow': 'Lime'
    }

    if not '
    return d[color_name_or_code.lower()] if color_name_or_code.lower() in d else color_name_or_code

    intcodes = [int(color_name_or_code[i:i + 2], 16) for i in range(1, len(color_name_or_code), 2)]
    if intcodes[0] <= intcodes[2] or intcodes[1] <= intcodes[2]:
        return color_name_or_code

    intcodes = sorted(intcodes)
    intcodes = map(lambda x: hex(x)[2:] if len(hex(x)[2:]) == 2 else '0' + hex(x)[2:], [intcodes[0], intcodes[2], intcodes[1]])
    intcodes = '

    return intcodes.upper() if any([c.isupper() for c in color_name_or_code]) else intcodes
