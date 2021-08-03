def solve(n, ddd):
    dsd = {d: i for i, d in enumerate(ddd)}
    child_cnt = [1] * n
    child_dist = [0] * n
    buf = []
    srt = sorted(list(dsd.items()), reverse=True)
    for d, i in srt[:-1]:
        cc = child_cnt[i]
        pd = d - (n - cc * 2)
        if pd == d or pd not in dsd:
            return -1
        pi = dsd[pd]
        buf.append((pi + 1, i + 1))
        child_cnt[pi] += cc
        child_dist[pi] += child_dist[i] + cc

    md, mi = srt[-1]
    if md != child_dist[mi]:
        return -1
    return buf


n = int(input())
ddd = list(map(int, (input() for _ in range(n))))
res = solve(n, ddd)
if res == -1:
    print((-1))
else:
    print(('\n'.join('{} {}'.format(*l) for l in res)))
