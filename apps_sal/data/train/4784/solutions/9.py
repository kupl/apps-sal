def image2ascii(image):
    glyphs = ' .,:;xyYX'

    def conv(c):
        return glyphs[c * (len(glyphs) - 1) // 255]
    return '\n'.join([''.join([conv(c) for c in row]) for row in image])
