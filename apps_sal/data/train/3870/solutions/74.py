def solve(s):
    pos = []
    for i in range(len(s)):
        pos.append('')
        if s[i] == ' ':
            pos[i] = ' '
    j = len(s) - 1
    i = 0
    while i < len(s):
        if pos[i] == ' ':
            if s[j] == ' ':
                j = j - 1
                i = i + 1
            else:
                i = i + 1
        else:
            if s[j] != ' ':
                pos[i] = s[j]
                j = j - 1
                i = i + 1
            else:
                j = j - 1
    return ''.join(pos)
