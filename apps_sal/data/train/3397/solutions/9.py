def grille(message, code):
    return ''.join(c for i, c in enumerate(message) if 1 << (len(message) - i - 1) & code)
