def is_alt(s):
    return helper(s, 0, 1) if s[0] in "aeiou" else helper(s, 1, 0)


def helper(s, n, m):
    for i in range(n, len(s), 2):
        if s[i] not in "aeiou":
            return False
    for i in range(m, len(s), 2):
        if s[i] in "aeiou":
            return False
    return True
