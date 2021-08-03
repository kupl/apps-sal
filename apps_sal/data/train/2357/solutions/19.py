def M(): return map(int, input().split())


n, m = M()
a = sum(list(M()))
d = 10**9 + 7
l = 1
r = 1
for i in range(n + a):
    l, r = l * (n + m - i) % d, r * (i + 1) % d
print(l * pow(r, d - 2, d) % d)
