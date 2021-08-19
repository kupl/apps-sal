REGION = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,:;-?! '()$%&" + '"'


def decrypt(encrypted_text):
    if not encrypted_text:
        return encrypted_text
    if any([x not in REGION for x in encrypted_text]):
        raise Exception
    three = REGION[::-1][REGION.index(encrypted_text[0])] + encrypted_text[1:]
    two = three[0]
    for i in range(1, len(three)):
        two += REGION[-REGION.index(three[i]) + REGION.index(two[i - 1])]
    return ''.join([x.swapcase() if i % 2 else x for (i, x) in enumerate(two)])


def encrypt(text):
    if not text:
        return text
    if any([x not in REGION for x in text]):
        raise Exception
    one = ''.join([x.swapcase() if i % 2 else x for (i, x) in enumerate(text)])
    two = ''.join([REGION[REGION.index(one[i - 1]) - REGION.index(x)] if i != 0 else x for (i, x) in enumerate(one)])
    return REGION[::-1][REGION.index(two[0])] + two[1:]
