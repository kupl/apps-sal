def encrypt(text, key):
    (r1, r2, r3) = ('qwertyuiop', 'asdfghjkl', 'zxcvbnm,.')
    (R1, R2, R3) = ('QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM<>')
    key = str(key).zfill(3)
    mx = ''
    for x in text:
        if x in r1:
            mx += r1[(r1.index(x) + int(key[0])) % 10]
        elif x in R1:
            mx += R1[(R1.index(x) + int(key[0])) % 10]
        elif x in r2:
            mx += r2[(r2.index(x) + int(key[1])) % 9]
        elif x in R2:
            mx += R2[(R2.index(x) + int(key[1])) % 9]
        elif x in r3:
            mx += r3[(r3.index(x) + int(key[2])) % 9]
        elif x in R3:
            mx += R3[(R3.index(x) + int(key[2])) % 9]
        else:
            mx += x
    return mx


def decrypt(text, key):
    (r1, r2, r3) = ('qwertyuiop', 'asdfghjkl', 'zxcvbnm,.')
    (R1, R2, R3) = ('QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM<>')
    key = str(key).zfill(3)
    mx = ''
    for x in text:
        if x in r1:
            mx += r1[(r1.index(x) - int(key[0])) % 10]
        elif x in R1:
            mx += R1[(R1.index(x) - int(key[0])) % 10]
        elif x in r2:
            mx += r2[(r2.index(x) - int(key[1])) % 9]
        elif x in R2:
            mx += R2[(R2.index(x) - int(key[1])) % 9]
        elif x in r3:
            mx += r3[(r3.index(x) - int(key[2])) % 9]
        elif x in R3:
            mx += R3[(R3.index(x) - int(key[2])) % 9]
        else:
            mx += x
    return mx
