def in_centre(s, i):
    return s[i] == 'a' and s[i + 1] == 'b' and (s[i + 2] == 'c')


def is_in_middle(s):
    if 'abc' not in s or len(s) < 3:
        return False
    l = len(s)
    if l % 2 == 1:
        i = (l + 1) // 2 - 2
        return in_centre(s, i)
    else:
        i1 = l // 2 - 2
        i2 = l // 2 - 1
        return in_centre(s, i1) or in_centre(s, i2)
