n = int(input())
a = [int(x) for x in input().split()]
b = int(input())
z = []
if b < n:
    for i in range(b):
        s = sum(a[:i]) + sum(a[n - b + i:])
        z.append(s)
    print(max(z))
else:
    print(sum(a))
