GLYPHS = ' .,:;xyYX'


def image2ascii(image):
    return '\n'.join((''.join((GLYPHS[x * 8 // 255] for x in row)) for row in image))
