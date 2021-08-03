n = 1 << int(input())
a = [[0, int(s)]for s in input().split()]
j = 1
while m := n - j:
    for i in range(n):
        if i & j:
            a[i] = sorted(a[i] + a[i ^ j])[2:]
    j *= 2
for s, f in a[1:]:
    print(m := max(m, s + f))
