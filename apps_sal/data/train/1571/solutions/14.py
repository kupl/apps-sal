def gcd(A, B):
    if B == 0:
        return A
    else:
        return gcd(B, A % B)


t = int(input())

for _ in range(t):
    n, a, k = list(map(int, input().split()))
    # d = /(n*(n-1))
    num = a * (n * (n - 1)) + (k - 1) * (360 * (n - 2) - 2 * a * n)
    den = n * (n - 1)
    print(f"{num//gcd(num, den)} {den//gcd(num, den)}")
