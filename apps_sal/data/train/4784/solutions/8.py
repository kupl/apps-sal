def image2ascii(i):
    return '\n'.join((''.join((glyphs[c * (len(glyphs) - 1) // 255] for c in r)) for r in i))
