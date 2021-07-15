def solve(s):
    spaces = []
    string = ''
    for i in range(len(s)):
        if s[i] == ' ':
            spaces.append(i - len(spaces))
    s1 = s.replace(' ', '')
    s1 = list(s1[-1::-1])
    for i in range(len(s1)):
        if i in spaces:
            string += ' '
        string += s1.pop(0)
    return string + ' ' if s[-1] == ' ' else string
