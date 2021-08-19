def solve(s, k):
    for c in 'abcdefghijklmnopqrstuvwxyz':
        n = s.count(c)
        s = s.replace(c, '', k)
        k -= n
        if k < 1:
            break
    return s
