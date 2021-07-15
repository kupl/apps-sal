def string_to_number(s):
    if s[0] != '-':
        d = 1
    else:
        d = -1
        s = s[1:]
    num = 0
    for c in range(len(s)-1, -1, -1):
            num += int(s[c])*d
            d *= 10
    return num
