def caesar_crypto_encode(text, shift):
    if not text or not text.strip():
        return ''
    a = 'abcdefghijklmnopqrstuvwxyz'
    a += a.upper()
    shift %= len(a)
    b = a[shift:] + a[:shift]
    return text.translate(str.maketrans(a, b))
