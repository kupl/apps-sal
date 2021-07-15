R = lambda: map(int, input().split())

n = int(input())
arr = [-1] + list(R()) + [-1]
dpl, dpr = arr[:], arr[:]
for i in range(1, n + 1):
    dpl[i] = max(0, min(dpl[i - 1] + 1, arr[i] - 1))
for i in range(n, 0, -1):
    dpr[i] = max(0, min(dpr[i + 1] + 1, arr[i] - 1))
print(1 + max(min(l, r) for l, r in zip(dpl, dpr)))
