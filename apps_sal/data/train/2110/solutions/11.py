N = int(1000000.0 + 100)
n = int(input())
arr = list(map(int, input().split()))
cnt = [0] * N
for i in arr:
    cnt[i] += 1
(res, s) = (0, 0)
for i in range(N):
    s += cnt[i]
    res += s % 2
    s //= 2
print(res)
