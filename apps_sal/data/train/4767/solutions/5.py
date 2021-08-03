from operator import gt, lt


def longest_comb(arr, command):
    cond = lt if command in ('< <', '<<') else gt
    lst = [[]]
    for a in arr:
        u = []
        for l in lst:
            if not l:
                u.append([a])
            else:
                if cond(l[-1], a):
                    u.append(l + [a])
            u.append(l)
        lst = u
    m_len = max(len(max(lst, key=len)), 3)
    ans = [l for l in lst if len(l) == m_len]
    return ans[0] if len(ans) == 1 else ans
