def string_to_number(s):
    neg = s[0] == '-'
    num = 0
    i = 0
    if neg:
        i = 1
    while i < len(s):
        num = num * 10 + (ord(s[i]) - ord('0'))
        i += 1
    return (-1 if neg else 1) * num
