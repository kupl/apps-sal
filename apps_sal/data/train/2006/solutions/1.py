from fractions import gcd
n = int(input())
a = list(map(int, input().split()))
mel = max(a)
for i in range(1, len(a)):
    a[0] = gcd(a[0], a[i])
print(('Bob', 'Alice')[(mel // a[0] - n) % 2])
