def solve(s):
    if s.count(' ') >= 1:
        positions = [i for i in range(len(s)) if s[i] == ' ']
        l = [i for i in s if i != ' '][::-1]
        for i in positions:
            l.insert(i, ' ')
        return ''.join(l)
    else:
        return s[::-1]
