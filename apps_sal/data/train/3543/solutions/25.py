def increment_string(strng):
    y = ''
    for x in range(len(strng) - 1, -1, -1):
        if strng[x].isnumeric():
            y = strng[x] + y
        else:
            break
    l = len(y)
    if l == 0:
        y = '1'
    else:
        y = str(int(y) + 1)
    if len(y) <= l:
        y = '0' * (l - len(y)) + y
    strng = strng[0:len(strng) - l] + y
    return strng
