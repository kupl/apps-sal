from collections import Counter

N = int(input())
A = list(map(int, input().split()))

ans = 0

b = [A[0]]

for i in range(1, N):
    b.append(b[-1] + A[i])

cnt = Counter(b)
cnt[0] += 1

for v in cnt.values():
    ans += v * (v - 1) // 2

print(ans)
