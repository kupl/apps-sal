def decrypt(text, n):
    if text == None:
        return text
    decodeList = encrypt(list(range(len(text))), n)
    return ''.join((text[decodeList.index(i)] for i in range(len(text))))


def encrypt(text, n):
    if text == None:
        return text
    return encrypt(text[1::2] + text[0::2], n - 1) if n > 0 else text
