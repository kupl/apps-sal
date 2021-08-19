def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


a = int(input())
b = list(map(int, input().split()))
c = m = 0
for x in b:
    c = gcd(c, x)
    if x > m:
        m = x
if m // c - a & 1:
    print('Alice')
else:
    print('Bob')
