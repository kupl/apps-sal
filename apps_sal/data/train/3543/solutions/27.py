def increment_string(strng):
    s, m = strng[::-1], ''
    for i in s:
        if i.isdigit():
            m = i + m
            strng = strng[:-1]
        else:
            break
    if m == '':
        return strng + '1'
    n = str(int(m) + 1)
    if len(n) < len(m):
        n = '0' * (len(m) - len(n)) + n
    return strng + n
