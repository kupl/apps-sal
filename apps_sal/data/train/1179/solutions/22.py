import math


def comb(n):
    return n * (n - 1) // 2


t = int(input())
while t > 0:
    ans = 0
    n = int(input())
    total = n * (n + 1) >> 1
    if total & 1 == 0:
        pivot = math.floor((-1 + math.sqrt(1 + 4 * total)) / 2)
        ans += n - pivot
        if pivot * (pivot + 1) >> 1 == total >> 1:
            ans += comb(pivot) + comb(n - pivot)
    print(ans)
    t -= 1
