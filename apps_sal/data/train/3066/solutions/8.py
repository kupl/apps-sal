def solve(s):
    sign, res, x = [], [], False
    for c in s:
        if c in '()-+':
            if c == '(': sign.append(x)
            elif c == ')': del sign[-1]
            x = c=='-'
        else:
            res.append('+-'[sum(sign)%2 ^ x])
            res.append(c)
    return ''.join(res).lstrip('+')
