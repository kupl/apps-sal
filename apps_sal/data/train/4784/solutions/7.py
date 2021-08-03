def image2ascii(i): return '\n'.join(''.join(glyphs[c * (len(glyphs) - 1) // MAX] for c in r) for r in i)
