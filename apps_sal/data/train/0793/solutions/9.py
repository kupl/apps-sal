def gcd_(a, b):
    if b == 0:
        return a
    else:
        return gcd_(b, a % b)


def lcm(a, b):
    return a * b // gcd_(a, b)


n, r = map(int, input().split())
l = list(map(int, input().split()))
k = []
for i in range(n):
    k.append(l[i] - r)
gcd = k[0]
for i in range(1, len(k)):
    gcd = gcd_(gcd, k[i])
print(gcd)
