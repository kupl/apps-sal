image2ascii = lambda i: '\n'.join(''.join(glyphs[c*(len(glyphs)-1)//MAX] for c in r) for r in i)
