def solve(st, a, b):
    return f'{st[:a]}{st[a:b + 1][::-1]}{st[b + 1:]}'
