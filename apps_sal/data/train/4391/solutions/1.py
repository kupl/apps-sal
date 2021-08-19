COLORDICT = {'gold': 'ForestGreen', 'khaki': 'LimeGreen', 'lemonchiffon': 'PaleGreen', 'lightgoldenrodyellow': 'SpringGreen', 'lightyellow': 'MintCream', 'palegoldenrod': 'LightGreen', 'yellow': 'Lime'}


def yellow_be_gone(clrIn):
    if '#' == clrIn[0]:
        (R, G, B) = (clrIn[1:3], clrIn[3:5], clrIn[5:7])
        if R > B and G > B:
            return '#' + B + G + R if R < G else '#' + B + R + G
    for clr in COLORDICT.keys():
        if clr == clrIn.lower():
            return COLORDICT[clr]
    return clrIn
