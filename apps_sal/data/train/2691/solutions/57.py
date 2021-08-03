def solve(s):
    t = ''.join([i if i.isnumeric() else ' ' for i in s])
    return max([int(i) for i in t.split(' ') if i])
