def grille(s, code):
    return ''.join(c for c, k in zip(s[::-1], bin(code)[2:][::-1]) if k == '1')[::-1]
