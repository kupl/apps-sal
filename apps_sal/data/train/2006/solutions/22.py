from fractions import gcd
n = int(input())
a = list(map(int, input().split()))
a.sort()
x = a[0]
for i in range(1, n):
    x = gcd(x, a[i])
moves = max(a) // x - n
if moves % 2 == 0:
    print('Bob')
else:
    print('Alice')
