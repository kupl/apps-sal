from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

d = defaultdict(lambda: (n, 0))
for i, a in enumerate(A):
    min_id, cnt = d[a]
    d[a] = (min(min_id, i), cnt + 1)

B = list(d.items())
B.sort()


ans = [0] * n
while True:
    a1, (m1, c1) = B.pop()
    if not B:
        ans[m1] += c1 * a1
        break
    a2, (m2, c2) = B[-1]
    ans[m1] += c1 * (a1 - a2)
    B[-1] = (a2, (min(m1, m2), c1 + c2))

print(*ans, sep='\n')
