def get_func(s, i):
    p2, p3 = '', ''
    s2, s3 = s[i:i + 2], s[i: i + 3]
    if s2[0] == s2[-1]:
        p2 = s2
        u, v = i - 1, i + 2
        while(u > -1 and v < len(s)):
            if s[u] != s[v]:
                break
            p2 = s[u] + p2 + s[v]
            u, v = u - 1, v + 1
    if s3[0] == s3[-1]:
        p3 = s3
        u, v = i - 1, i + 3
        while(u > -1 and v < len(s)):
            if s[u] != s[v]:
                break
            p3 = s[u] + p3 + s[v]
            u, v = u - 1, v + 1
    return p3 if len(p3) > len(p2) else p2


def set_pal(p, idxp, pal, idx):
    if len(p) > len(pal) or (len(p) == len(pal) and idxp < idx):
        pal, idx = p, idxp
    return pal, idx


def longest_palindrome(s):
    if len(s) < 2:
        return s
    pal = s[0]
    idx = 1
    j = len(s) // 2 - 1
    k = j + 1
    if len(s) > 3:
        for i in range(j):
            pal, idx = set_pal(get_func(s, j - i - 1), j - i, pal, idx)
            pal, idx = set_pal(get_func(s, k + i - 1), k + i, pal, idx)
            if len(s) < len(pal) + 2 * i:
                break
    if len(pal) < 3 and len(s) % 2 != 0:
        pal, idx = set_pal(get_func(s, len(s) - 3), len(s) - 2, pal, idx)
    if len(pal) < 2:
        sub = s[len(s) - 2:len(s)]
        if sub[0] == sub[-1]:
            pal = sub
    return pal
