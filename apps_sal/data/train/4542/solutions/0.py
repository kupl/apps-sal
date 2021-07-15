from string import ascii_letters as az


def caesar_crypto_encode(text, shift):
    if not text:
        return ''
    sh = shift % 52
    return str.translate(text, str.maketrans(az, az[sh:] + az[:sh])).strip()
