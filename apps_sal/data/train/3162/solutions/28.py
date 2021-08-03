def compare(s1, s2):
    return chsum(s1) == chsum(s2)


def chsum(s):
    if not s:
        return 0

    s = s.upper()
    if any(c < 'A' or c > 'Z' for c in s):
        return 0

    return sum(ord(c) for c in s)
