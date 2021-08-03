def middle_permutation(s):
    s = ''.join(sorted(s))
    m = int(len(s) / 2)
    x = s[m - 1:m + 1] if len(s) % 2 else s[m - 1]

    return (s.replace(x, '') + x)[::-1]
