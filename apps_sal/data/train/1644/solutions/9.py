b91_enctab = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '
    '%', '&', '(', ')', '*', '+', ',', '.', '/', ':', ';', '<', '=',
    '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~', '"'
]


def b91decode(strng):
    decode_str = ""
    value = -1
    seek = 0
    bynary = 0

    for item in strng:
        code = b91_enctab.index(item)
        if value < 0:
            value = code
        else:
            value += code * 91
            bynary |= value << seek

            if value & 8191 > 88:
                seek += 13
            else:
                seek += 14

            while seek > 7:
                decode_str += chr(bynary & 255)
                bynary >>= 8
                seek -= 8
            value = -1
    if value + 1:
        decode_str += chr((bynary | value << seek) & 255)
    return decode_str


def b91encode(strng):
    encode_str = ''
    bynary = 0
    seek = 0
    for symb in strng:
        bynary |= ord(symb) << seek
        seek += 8
        if seek > 13:
            value = bynary & 8191

            if value <= 88:
                value = bynary & 16383
                bynary >>= 14
                seek -= 14
            else:
                bynary >>= 13
                seek -= 13

            encode_str += b91_enctab[value % 91] + b91_enctab[value // 91]

    if seek != 0:
        encode_str += b91_enctab[bynary % 91]
        if seek > 7 or bynary > 90:
            encode_str += b91_enctab[bynary // 91]

    return encode_str


a = """<txG@<^F


r = """4J > StI @ i5oLyF.Th)8=+!tB9!


a= '''4J>StI@i5oLyF.Th)8=+!tB9!

print((b91encode('<txG@<^F

print((r == b91encode(a)))
