def solve(s):
    y = s.replace(' ', '')
    backwards = y[::-1]
    c = 0
    d = 0
    solution = ''
    for i in range(0, len(s)):
        if s[i] == ' ':
            solution += ' '
            c = c + 1
        else:
            solution += backwards[i - c]
    return solution
