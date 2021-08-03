from fractions import gcd
n = int(input())
a = [int(x) for x in input().split()]
gg = a[0]
for i in range(1, n):
    gg = gcd(gg, a[i])
for i in range(n):
    a[i] //= gg
if (max(a) - n) % 2 == 0:
    print('Bob')
else:
    print('Alice')
