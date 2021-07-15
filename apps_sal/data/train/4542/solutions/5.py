def caesar_crypto_encode(text, shift):
    if text in ("", None):
        return ""
    else:
        from string import ascii_letters as abc
        text = text.strip()
        shift = (shift - 1) % len(abc) + 1
        return text.translate(str.maketrans(abc, abc[shift:] + abc[:shift]))
