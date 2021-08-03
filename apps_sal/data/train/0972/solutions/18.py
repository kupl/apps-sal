n, k = list(map(int, input().split()))
h = []
for _ in range(n):
    h.append(int(input()))

h = sorted(h)
mm = 10**8
for i in range(n - k):
    mm = min(mm, h[i + k - 1] - h[i])

print(mm)
