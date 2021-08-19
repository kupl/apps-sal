import string
reg = string.ascii_uppercase + string.ascii_lowercase + string.digits + '.,:;-?! \'()$%&"'


def decrypt(text):
    if not text:
        return text
    for i in text:
        if i not in reg:
            raise Exception
    dec = [reg[reg[::-1].index(text[0])]]
    for i in range(1, len(text)):
        tem = reg.index(text[i])
        ad = abs(tem - 77) + reg.index(dec[-1])
        if ad < 77:
            dec.append(reg[ad])
        else:
            dec.append(reg[ad - 77])
    for i in range(1, len(dec), 2):
        dec[i] = dec[i].swapcase()
    return ''.join(dec)


def encrypt(text):
    if not text:
        return text
    for i in text:
        if i not in reg:
            raise Exception
    (a, enc) = (list(text), [reg[-(reg.index(text[0]) + 1)]])
    for i in range(1, len(a), 2):
        a[i] = a[i].swapcase()
    for i in range(1, len(a)):
        ind = reg.index(a[i - 1]) - reg.index(a[i])
        enc.append(reg[ind])
    return ''.join(enc)
