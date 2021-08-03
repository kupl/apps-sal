def color_2_grey(colors):
    return [[[int(round(sum(rgb) / 3))] * 3 for rgb in row] for row in colors]
