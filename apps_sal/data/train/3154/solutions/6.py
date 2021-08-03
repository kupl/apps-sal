def color_2_grey(colors):
    return [[[round(sum(pixel) / 3)] * 3 for pixel in line] for line in colors]
