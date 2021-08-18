from bisect import bisect_left

n = int(input())
s = list(input())
q = int(input())
query = [input() for _ in range(q)]

p = [[] for _ in range(26)]

for i, x in enumerate(s):
    p[ord(x) - ord('a')].append(i)

for x in query:
    a, b, c = x.split()
    if a == '1':
        b = int(b) - 1
        if s[b] == c:
            continue
        d = ord(s[b]) - ord('a')
        e = ord(c) - ord('a')
        temp = bisect_left(p[d], b)
        p[d].pop(temp)
        temp = bisect_left(p[e], b)
        p[e].insert(temp, b)
        s[b] = c
    else:
        b = int(b) - 1
        c = int(c) - 1
        ans = 0
        for i in range(26):
            L = bisect_left(p[i], b)
            if L >= len(p[i]):
                continue
            if p[i][L] <= c:
                ans += 1
        print(ans)
