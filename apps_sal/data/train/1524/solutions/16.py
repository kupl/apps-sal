t = int(input())


def haha(x, y, p):
    ans = 1
    x = x % p
    while y > 0:
        if y % 2 != 0:
            ans = ans * x % p
        y = y / 2
        x = x ** 2 % p
    return ans


while t > 0:
    t -= 1
    (n, k) = list(map(int, input().split()))
    m = 1000000007
    print(k % m * haha(k - 1, n - 1, m) % m % m)
