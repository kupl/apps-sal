def solve(s):
    rev_s = ''.join(s.split())[::-1]
    res = []
    n = 0
    for i in [len(w) for w in s.split(' ')]:
        if i == 0:
            res.append('')
        else:
            res.append(rev_s[n:n + i])
        n += i
    return ' '.join(res)
