def get_pal(s):
    if len(s) == 1:
        return 0
    if len(s) == 2 and s[0] == s[1]:
        return 0
    elif len(s) == 2 and s[0] != s[1]:
        return 1
    return 1 + min(get_pal(s[1:]), get_pal(s[:-1])) if s[0] != s[-1] else get_pal(s[1:-1])


def solve(s):
    ans = get_pal(s)
    return "OK" if ans == 0 else "remove one" if ans == 1 else "not possible"
