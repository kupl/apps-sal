(a, n, k) = list(map(int, input().split()))
l = []
c = 0
while c != k:
    x = a % (n + 1)
    l.append(x)
    a = a // (n + 1)
    c += 1
print(*l)
