def solve(s):
    print(s)
    return True if len([x for y, x in enumerate(s) if s[y] != s[-(y + 1)]]) == 2 else True if (len(s) % 2 and not [x for y, x in enumerate(s) if s[y] != s[-(y + 1)]]) else False
