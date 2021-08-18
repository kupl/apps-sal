def longest(s1, s2):

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    s = s1 + s2

    y = ""

    for x in alphabet:
        if x not in s:
            continue
        if x in s:
            y = y + x

    return y
