j = n = 1 << int(input())
a = [[int(s)] for s in input().split()]
while j > 1:
    j >>= 1
    a = [sorted(a[i] + a[i ^ j] * (i & j > 0))[-2:] for i in range(n)]
for (s, f) in a[1:]:
    j = max(j, s + f)
    print(j)
