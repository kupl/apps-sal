from string import ascii_uppercase as letters


def encrypt(text, key):
    key = [[letters.index(c) for c in key.upper()[i:i + 2]] for i in (0, 2)]
    text = [letters.index(c) for c in text.upper() if c.isalpha()]
    if len(text) % 2 != 0:
        text.append(letters.index('Z'))
    out = []
    for i in range(0, len(text), 2):
        for j in range(2):
            out.append((key[j][0] * text[i] + key[j][1] * text[i + 1]) % 26)
    return ''.join((letters[n] for n in out))
