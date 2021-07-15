def solve(s):
    a = [s.replace(s[y], '', 1) for y,x in enumerate(s)]
    return any(len(sorted(set([x.count(c) for c in x]))) == 1 for x in a)
