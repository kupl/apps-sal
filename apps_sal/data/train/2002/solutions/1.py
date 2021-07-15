str = input()
l = len(str)
a = [0] * (2 * l)
pos = [[] for i in range(26)]
for i, c in enumerate(str):
    t = ord(c) - ord('a')
    a[i] = t
    a[i + l] = t
    pos[t].append(i)
ans = 0
for c in range(26):
    cur = 0
    for k in range(1, l):
        cnt = [0] * 26
        for i in pos[c]:
            cnt[a[i + k]] += 1
        tot = 0
        for i in cnt:
            if i == 1:
                tot += 1
        cur = max(cur, tot)
    ans += cur
print(ans / l)

