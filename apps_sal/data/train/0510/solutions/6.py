import bisect

n = int(input())
s = list(input())
q = int(input())

pos = [[] for i in range(26)]
alp = "abcdefghijklmnopqrstuvwxyz"
atoi = {}
for i in range(26):
    atoi[alp[i]] = i
for i in range(n):
    pos[atoi[s[i]]].append(i)

for i in range(q):
    a, b, c = input().split()
    if a == "1":
        b = int(b)-1
        if c == s[b]:
            continue
        index = bisect.bisect_left(pos[atoi[s[b]]], b)
        del pos[atoi[s[b]]][index]
        bisect.insort_left(pos[atoi[c]], b)
        s[b] = c
    else:
        l, r = int(b)-1, int(c)
        ans = 0
        for i in range(26):
            cnt = bisect.bisect_left(pos[i], r) - bisect.bisect_left(pos[i], l)
            if cnt > 0:
                ans += 1
        print(ans)
