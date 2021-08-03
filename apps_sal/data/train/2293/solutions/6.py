j = n = 1 << int(input())
a = [[0, int(s)]for s in input().split()]
while j > 1:
    j >>= 1
    for i in range(n):
        if i & j:
            a[i] = sorted(a[i] + a[i ^ j])[2:]
for s, f in a[1:]:
    print(j := max(j, s + f))
