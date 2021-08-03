def solve(s):
    vow, con = [], []
    for c in s:
        if c in 'aeiou':
            vow.append(c)
        else:
            con.append(c)

    len_v, len_c = len(vow), len(con)

    if len_v - len_c in [0, 1]:
        return ''.join(v + c for v, c in zip(sorted(vow), sorted(con) + ['']))
    elif len_v - len_c == -1:
        return ''.join(v + c for v, c in zip(sorted(con), sorted(vow) + ['']))

    return 'failed'
