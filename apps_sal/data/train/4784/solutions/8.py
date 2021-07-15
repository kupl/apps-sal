image2ascii = lambda i: '\n'.join(''.join(glyphs[c*(len(glyphs)-1)//255] for c in r) for r in i)
