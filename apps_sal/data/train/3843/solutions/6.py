from string import ascii_uppercase, ascii_lowercase, digits
s_Base = ascii_uppercase + ascii_lowercase + digits + '.,:;-?! \'()$%&"'


def decrypt(text):
    if not text:
        return text
    text = s_Base[-(s_Base.index(text[0]) + 1)] + text[1:]
    for (index, letter) in enumerate(text[1:]):
        x = s_Base.index(text[index])
        y = s_Base.index(letter)
        diff = x - y if x - y >= 0 else x - y + 77
        text = text[:index + 1] + s_Base[diff] + text[index + 2:]
    return ''.join((letter.swapcase() if index % 2 != 0 else letter for (index, letter) in enumerate(text)))


def encrypt(text):
    if not text:
        return text
    for letter in text:
        if letter not in s_Base:
            raise ValueError
    text = ''.join((letter.swapcase() if index % 2 != 0 else letter for (index, letter) in enumerate(text)))
    for (index, letter) in enumerate(text[1:]):
        if index == 0:
            x = s_Base.index(text[index])
        y = s_Base.index(letter)
        diff = x - y if x - y >= 0 else x - y + 77
        x = y
        text = text[:index + 1] + s_Base[diff] + text[index + 2:]
    text = s_Base[-(s_Base.index(text[0]) + 1)] + text[1:]
    return text
