def color_2_grey(colors):
    return [[[round((r + g + b) / 3)] * 3 for r, g, b in row] for row in colors]
