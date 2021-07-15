from string import ascii_letters

def caesar_crypto_encode(text, shift):
    return '' if text is None or text.isspace() \
        else text.translate(str.maketrans(ascii_letters, ascii_letters[shift % 52:] + ascii_letters[:shift % 52]))
