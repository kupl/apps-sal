def string_to_number(s):
    x = 0
    yygq = 1 if s[0] == "-" else 0
    for i in range(yygq, len(s)):
        x += (ord(s[i]) - 48) * 10**(len(s) - i - 1)
    return -x if yygq == 1 else x
