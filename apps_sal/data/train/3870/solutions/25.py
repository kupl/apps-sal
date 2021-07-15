def solve(s):
    print(s)
    l = [c for c in s if c != ' ']
    l.reverse()
    for i,c in enumerate(s):
        if c == ' ':
            l.insert(i, c)
    return ''.join(l)
