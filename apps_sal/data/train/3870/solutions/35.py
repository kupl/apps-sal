def solve(s):
    new = list(s.replace(' ', '')[::-1])
    [new.insert(i, ' ') for i, j in enumerate(s) if j == ' ']
    return ''.join(new)
