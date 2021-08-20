from collections import defaultdict
N = int(input())
a = list(map(int, input().split()))
s = [0]
for i in range(N):
    s.append(s[-1] ^ a[i])
D1 = defaultdict(int)
D2 = defaultdict(int)
ans = 0
for i in range(N + 1):
    if i % 2 == 0:
        ans += D1[s[i]]
        D1[s[i]] += 1
    else:
        ans += D2[s[i]]
        D2[s[i]] += 1
print(ans)
