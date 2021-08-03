def solve(s, i):
    c = s[i] == '('
    if not c:
        return -1
    while c != 0 and i != len(s):
        i += 1
        if s[i] == '(':
            c += 1
        elif s[i] == ')':
            c -= 1
    return -1 if c != 0 else i
