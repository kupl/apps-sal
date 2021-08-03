n, k = tuple(map(int, input().split()))
h = []
for i in range(n):
    h.append(int(input()))
h.sort()
dhmin = 10e9
for i in range(n - k + 1):
    temp = h[i + k - 1] - h[i]
    dhmin = temp if temp < dhmin else dhmin
print(dhmin)
