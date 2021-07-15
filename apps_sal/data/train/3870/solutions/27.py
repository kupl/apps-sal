def solve(s):
    s_ = list(''.join(s.split())[::-1])
    for i, l in enumerate(s):
        if l == ' ':
            s_.insert(i, l)
    return ''.join(s_)
