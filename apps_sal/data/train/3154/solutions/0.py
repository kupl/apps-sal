from statistics import mean

def grey(rgb):
    return [int(round(mean(rgb)))]*3

def color_2_grey(colors):
    return [[grey(pixel) for pixel in row] for row in colors]
