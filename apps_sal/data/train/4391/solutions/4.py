SHADES = {
    "gold": "ForestGreen",
    "khaki": "LimeGreen",
    "lemonchiffon": "PaleGreen",
    "lightgoldenrodyellow": "SpringGreen",
    "lightyellow": "MintCream",
    "palegoldenrod": "LightGreen",
    "yellow": "Lime"
}


def yellow_be_gone(color):
    if color[0] == '
    r, g, b = color[1:3], color[3:5], color[5:]
    if r > b and g > b:
        color = '
    return SHADES.get(color.lower(), color)
