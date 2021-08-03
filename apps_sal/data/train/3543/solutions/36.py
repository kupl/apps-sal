def increment_string(strng):
    if strng == '':
        return '1'
    if not '0' <= strng[-1] <= '9':
        return strng + '1'
    if '0' <= strng[-1] < '9':
        return strng[:-1] + str(int(strng[-1]) + 1)
    i = -1
    while strng[i] == '9':
        i = i - 1
    if not '0' <= strng[i] < '9':
        return strng[:i + 1] + '1' + '0' * (-i - 1)
    return strng[:i] + str(int(strng[i]) + 1) + '0' * (-i - 1)
