def is_pal(s):
    return all((s[i] == s[len(s) - i - 1] for i in range(len(s) // 2)))


def solve(s):
    return any((is_pal(s[i:] + s[:i]) for i in range(len(s))))
