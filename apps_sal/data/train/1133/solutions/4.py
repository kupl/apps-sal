T = int(input())


def get_gcd(x, y):
    while y:
        (x, y) = (y, x % y)
    return x


for _ in range(T):
    N = int(input())
    num = list(map(int, input().split()))
    gcd = num[0]
    for n in num[1:]:
        gcd = get_gcd(gcd, n)
    print(gcd, sum(num) // gcd)
