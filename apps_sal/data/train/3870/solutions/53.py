def solve(s):
    spaces = []
    for i in range(len(s)):
        if s[i] == ' ':
            spaces.append(i)
    s = s.replace(' ', '')[::-1]
    while len(spaces) > 0:
        i = spaces.pop(0)
        s = s[:i] + ' ' + s[i:]
    return s
