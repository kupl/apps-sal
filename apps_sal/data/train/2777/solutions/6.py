def solve(st):
    strx = ''
    for i, x in enumerate(st):
        if x.isdigit():
            return strx + int(x) * solve(st[i + 1:])
        if x.isalpha():
            strx += x
    return strx
