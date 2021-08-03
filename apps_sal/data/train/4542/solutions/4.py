alpha = 'abcdefghijklmnopqrstuvwxyz'
alpha += alpha.upper()


def caesar_crypto_encode(text, shift):
    if not text or not text.strip():
        return ''

    return ''.join(
        alpha[(alpha.index(c) + shift) % 52]
        if c.isalpha() else c for c in text)
