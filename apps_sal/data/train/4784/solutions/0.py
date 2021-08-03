def image2ascii(image):
    return '\n'.join(''.join(glyphs[(v * 8) // 255] for v in r) for r in image)
