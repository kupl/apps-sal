def color_2_grey(colors):
    for line in colors:
        for pixel in line:
            grey = int((sum(pixel)/3)+0.5)
            pixel[0] = grey
            pixel[1] = grey
            pixel[2] = grey
    return colors
