def yellow_be_gone(color):
    color_change = {"gold": "ForestGreen", "khaki": "LimeGreen", "lemonchiffon": "PaleGreen", "lightgoldenrodyellow": "SpringGreen",
        "lightyellow": "MintCream", "palegoldenrod": "LightGreen", "yellow": "Lime"}
    if color.startswith("#"):
        codes = [(int(rgb, 16), rgb) for rgb in [color[1:3], color[3:5], color[5:]]]
        rgb_string = color if any(c <= codes[2][0] for c in (x for x, _ in codes[:2])) else\
            "#" + "{0}{2}{1}".format(*[c for _, c in sorted(codes)])
        return rgb_string
    return color_change.get(color.lower(), color)
