def middle_permutation(string):
    rev, l = sorted(string)[::-1], len(string)
    mid = rev[l // 2:l // 2 + l % 2 + 1]
    return ''.join(mid + [ch for ch in rev if ch not in mid])
