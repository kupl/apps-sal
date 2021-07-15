def solve(s):
    spaces = [i for i in range(len(s)) if s[i] == ' ']
    rev = list(s[::-1].replace(' ', ''))
    for v in spaces:
        rev.insert(v, ' ')
    return ''.join(rev)
