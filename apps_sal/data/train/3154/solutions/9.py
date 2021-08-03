def color_2_grey(colors):
    return [[[round((R + G + B) / 3)] * 3 for [R, G, B] in row] for row in colors]
