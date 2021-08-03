from bisect import bisect_left
import string

dic = {c: [] for c in string.ascii_lowercase}
N = int(input())
S = list(input())
Q = int(input())
for i in range(len(S)):
    dic[S[i]].append(i + 1)

for i in range(Q):
    a, b, c = list(map(str, input().split()))
    if a == '1':
        if S[int(b) - 1] == c:
            continue
        b = int(b)
        f = S[b - 1]
        d = bisect_left(dic[f], b)
        e = bisect_left(dic[c], b)
        dic[f].pop(d)
        dic[c].insert(e, b)
        S[b - 1] = c
    else:
        ans = 0
        b, c = int(b), int(c)
        for j in string.ascii_lowercase:
            d = bisect_left(dic[j], b)
            if d < len(dic[j]):
                if dic[j][d] <= c:
                    ans += 1
        print(ans)
