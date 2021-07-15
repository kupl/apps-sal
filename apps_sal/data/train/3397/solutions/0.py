def grille(msg, code):
    return ''.join(msg[-1-i] for i,c in enumerate(bin(code)[::-1]) if c == '1' and i < len(msg))[::-1]
