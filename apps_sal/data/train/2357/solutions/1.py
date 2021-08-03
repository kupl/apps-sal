n, m, *a = map(int, open(0).read().split())
d = 10**9 + 7
l = 1
r = 1
for i in range(n + sum(a)):
    l, r = l * (n + m - i) % d, r * (i + 1) % d
print(l * pow(r, d - 2, d) % d)
