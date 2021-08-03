import math
t = int(input())
while t > 0:
    t -= 1
    # n = int(input())
    a, m = list(map(int, input().split()))
    d = 1
    ans = set()
    limit = int(math.sqrt(m) + 1)
    while d < limit + 1:
        if m % d == 0:
            num = m // d - 1
            if num % a == 0:
                ans.add((num // a) * d)
            d2 = m // d
            num = m // d2 - 1
            if num > 0 and num % a == 0:
                ans.add((num // a) * d2)
        d += 1
    print(len(ans))
    print(*sorted(ans))
