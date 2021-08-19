import fractions
n = int(input())
a = list(map(int, input().split()))
gcd = a[0]
for i in range(1, n):
    gcd = fractions.gcd(gcd, a[i])
x = max(a) / gcd - n
if x % 2 == 1:
    print('Alice')
else:
    print('Bob')
