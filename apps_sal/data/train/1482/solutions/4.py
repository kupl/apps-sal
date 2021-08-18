def gcd(a, b):

    if (b == 0):
        return a
    return gcd(b, a % b)


t = int(input())

for _ in range(t):
    n = int(input())

    q = "1" + "0" * (n // 2)
    print(1, q)
