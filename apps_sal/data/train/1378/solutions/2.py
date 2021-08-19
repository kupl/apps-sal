(a, n, k) = list(map(int, input().split()))
s = []
while k:
    s.append(a % (n + 1))
    a = a // (n + 1)
    k -= 1
print(*s)
