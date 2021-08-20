def caesar_crypto_encode(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    offset = (shift % 52 + 52) % 52
    return ''.join([alphabet[(alphabet.find(ch) + offset) % 52] if ch in alphabet else ch for ch in text.strip()]) if text else ''
