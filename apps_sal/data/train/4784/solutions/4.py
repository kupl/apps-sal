glyphs = " .,:;xyYX"


def image2ascii(image):
    ratio = 255 / 8

    new_rows = list()
    for row in image:
        new_row = ''.join((glyphs[int(pixel // ratio)] for pixel in row))
        new_rows.append(new_row)

    return '\n'.join(new_rows)
