from fractions import gcd
n = int(input())
a = list(map(int, input().split()))
d = gcd(a[0], a[1])
for i in range(1, n, 1):
    d = gcd(d, a[i])
m2 = max(a)
if (m2 // d - n) % 2 == 1:
    print('Alice')
else:
    print('Bob')
