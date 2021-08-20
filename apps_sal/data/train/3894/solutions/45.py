import string


def solve(s):
    (low, up) = (string.ascii_lowercase, string.ascii_uppercase)
    (l_c, u_c) = (0, 0)
    for c in s:
        if c in low:
            l_c += 1
        else:
            u_c += 1
    if l_c >= u_c:
        return s.lower()
    elif l_c < u_c:
        return s.upper()
