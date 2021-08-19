def encode(message, key):
    (s1, s2) = ([], [])
    for (c1, c2) in zip(key[0::2], key[1::2]):
        s1.append(c1 + c1.upper())
        s2.append(c2 + c2.upper())
    return message.translate(str.maketrans(*map(''.join, [s1 + s2, s2 + s1])))


decode = encode
