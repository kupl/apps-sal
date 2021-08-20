from string import ascii_lowercase as low, ascii_uppercase as upp, digits as dig
trans = str.maketrans(low + upp + dig, low[13:] + low[:13] + upp[13:] + upp[:13] + dig[5:] + dig[:5])


def ROT135(input):
    return input.translate(trans)
