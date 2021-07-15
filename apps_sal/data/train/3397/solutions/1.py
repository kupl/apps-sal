def grille(message, code):
    binary = bin(code)[2:][-len(message):].zfill(len(message))
    return ''.join(char for char, code in zip(message, binary) if code == '1')
