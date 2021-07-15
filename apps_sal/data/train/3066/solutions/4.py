def solve(s):
    pos = [0]
    s = '(' + s + ')'
    def parse():
        sgn = -1 if s[pos[0]] == '-' else 1
        pos[0] += 2 if s[pos[0]] in ('+', '-') else 1
        lst = []
        while s[pos[0]] != ')':
            if '(' not in (s[pos[0]], s[pos[0]+1]):
                lst.append((-1 if s[pos[0]]=='-' else 1, s[pos[0]+1] if s[pos[0]] in ('+', '-') else s[pos[0]]))
                pos[0] += 2 if s[pos[0]] in ('+', '-') else 1
            else:
                lst.extend(parse())
        pos[0] += 1
        return [(t[0]*sgn, t[1]) for t in lst]
    return ''.join([('+' if t[0]==1 else '-') + t[1] for t in parse()]).lstrip('+')

