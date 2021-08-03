from string import ascii_lowercase, ascii_uppercase
S = ascii_lowercase + ascii_uppercase
D = {c: i for i, c in enumerate(S)}


def caesar_crypto_encode(text, shift):
    if text and text != ' ' * len(text):
        return ''.join(S[(D[c] + shift) % 52] if c in D else c for c in text)
    return ""
