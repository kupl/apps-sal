def solve(s):
    r = [',' if x in 'qwertyuioplkjhgfdsazxcvbnm' else x for x in s]
    t = list(filter(lambda x: x != '', ''.join(r).split(',')))
    return max(list(map(lambda x: int(x), t)))
