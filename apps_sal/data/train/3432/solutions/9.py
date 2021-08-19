def cipher(phrase: str):
    return ''.join((chr(ord('a') + (ord(c) - ord('a') + i % 3 + (i - 1) // 3) % 26) if i > 0 and c != ' ' else c for (i, c) in enumerate(phrase)))
