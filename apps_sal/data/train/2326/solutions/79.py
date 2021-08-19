n = int(input())
A = list(map(int, input().split()))
parent = [(0, -1)]
now = 0
for (i, a) in enumerate(A):
    if now < a:
        parent.append((a, i))
        now = a
A.sort()
ans = [0] * n
cnt = 0
p = parent[-1][1]
for a in A[::-1]:
    if parent[-1][0] >= a:
        p = parent[-1][1]
        ans[p] += cnt * (parent[-1][0] - parent[-2][0])
        parent.pop()
    if parent[-1][0] < a:
        cnt += 1
        ans[p] += a - parent[-1][0]
print('\n'.join((str(i) for i in ans)))
