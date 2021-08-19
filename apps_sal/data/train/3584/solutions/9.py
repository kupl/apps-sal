top = 'qwertyuiop'
top_caps = 'QWERTYUIOP'
mid = 'asdfghjkl'
mid_caps = 'ASDFGHJKL'
bot = 'zxcvbnm,.'
bot_caps = 'ZXCVBNM<>'


def encrypt(text, encryptKey):
    encryptKey = str(encryptKey).zfill(3)
    res = ''
    for char in text:
        for (i, row) in enumerate([top, top_caps, mid, mid_caps, bot, bot_caps]):
            if char in row:
                shift = int(encryptKey[i // 2])
                res += char.translate(str.maketrans(row, row[shift:] + row[:shift]))
                break
        else:
            res += char
    return res


def decrypt(text, encryptKey):
    encryptKey = str(encryptKey).zfill(3)
    res = ''
    for char in text:
        for (i, row) in enumerate([top, top_caps, mid, mid_caps, bot, bot_caps]):
            if char in row:
                shift = int(str(encryptKey)[i // 2])
                res += char.translate(str.maketrans(row, row[-shift:] + row[:-shift]))
                break
        else:
            res += char
    return res
