import bisect
n = int(input())
s = list(input())
alp = 'abcdefghijklmnopqrstuvwxyz'
cnt = {c: [] for c in alp}
for (i, c) in enumerate(s):
    cnt[c].append(i)
q = int(input())
for _ in range(q):
    (t, x, y) = input().split()
    ans = 0
    if t == '1':
        (i, c) = (int(x) - 1, y)
        if s[i] == c:
            continue
        a = bisect.bisect_left(cnt[s[i]], i)
        cnt[s[i]].pop(a)
        s[i] = c
        b = bisect.bisect_left(cnt[c], i)
        cnt[c].insert(b, i)
    else:
        (l, r) = (int(x) - 1, int(y) - 1)
        for c in alp:
            a = bisect.bisect_left(cnt[c], l)
            if a < len(cnt[c]) and cnt[c][a] <= r:
                ans += 1
        print(ans)
