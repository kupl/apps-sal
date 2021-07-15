from collections import defaultdict

N = int(input())
*a, = list(map(int, input().split()))

cnt = defaultdict(int)
pos = defaultdict(lambda :10**12)
ans = defaultdict(int)

for i, j in enumerate(a, start=1):
    pos[j] = min(pos[j], i)
    cnt[j] += 1

target = [list(i) for i in sorted(pos.items())][::-1]
size = len(target)

for i in range(len(target)-1):
    a, b = target[i]
    c, d = target[i+1]
    ans[b] += cnt[a]*(a-c)
    cnt[c] += cnt[a]
    cnt[a] = 0
    target[i+1][1] = min(target[i+1][1], b)

a = target[-1][0]
ans[1] += cnt[a]*a
for i in range(1, N+1):
    print((ans[i]))

