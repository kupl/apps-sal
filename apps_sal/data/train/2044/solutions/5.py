(n, k) = list(map(int, input().split()))
mid = n - k - 1
r = [0] * k
for i in range(n - 1):
    r[i % k] += 1
print(r[0] + r[1])
v1 = 2
ans = []
for i in range(k):
    v0 = 1
    for _ in range(r[i]):
        ans.append('%d %d' % (v0, v1))
        v0 = v1
        v1 += 1
print('\n'.join(ans))
