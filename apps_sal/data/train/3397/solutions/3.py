def grille(message, code):
    binary = bin(code)[2:][::-1]
    return ''.join([j for (i, j) in enumerate(message[::-1]) if i < len(binary) and binary[i] == '1'])[::-1]
