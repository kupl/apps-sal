def bears(x, s):
    result = []
    bears = []
    while len(s) > 1:
        if s[0] == 'B' and s[1] == '8':
            s = s[2:]
            bears.append('B8')
        elif s[0] == '8' and s[1] == 'B':
            s = s[2:]
            bears.append('8B')
        else:
            s = s[1:]
    result.append(''.join(bears))
    test = len(bears) * 2 >= x
    result.append(test)
    return result
