SPACE, NULL_STR = " ", ""


def rotate(n, s):
    if not s:
        return NULL_STR

    if SPACE in s:
        return SPACE.join(rotate(n, word) for word in s.split(SPACE))

    else:
        n %= len(s)
        return s[-n:] + s[:-n]


def cipher(n, s):
    # extract spaces
    spaces = [idx for idx, char in enumerate(s) if char == SPACE]

    for _ in range(abs(n)):
        # rotate words (decoding)
        if n < 0:
            s = rotate(n, s)

        # remove spaces, rotate string, put back spaces
        s = s.replace(SPACE, NULL_STR)
        s = rotate(n, s)
        for idx in spaces:
            s = s[:idx] + SPACE + s[idx:]

        # rotate words (encoding)
        if n > 0:
            s = rotate(n, s)

    return s


def encode(n, s):
    return str(n) + SPACE + cipher(n, s)


def decode(s):
    n, s = s.split(SPACE, 1)
    n = int(n)
    return cipher(-n, s)
