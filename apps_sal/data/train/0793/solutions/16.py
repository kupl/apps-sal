# cook your dish here
# cook your dish here
def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)


n, r = (input().split())
a = list(map(int, input().split()))
c = []
for i in range(len(a) - 1):
    c.append(a[i + 1] - a[i])
c.append(abs(a[0] - int(r)))
res = c[0]
for d in c[1::]:
    res = gcd(res, d)
print(res)
