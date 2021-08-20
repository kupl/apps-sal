def gcdf(x, y):
    while y:
        (x, y) = (y, x % y)
    return x


t = int(input())
for cases in range(t):
    (n, m) = list(map(int, input().split()))
    spells = list(map(int, input().split()))
    kills = 0
    gcd = spells[0]
    for i in range(1, m):
        gcd = gcdf(gcd, spells[i])
    if n > gcd:
        kills += n - gcd
        n = gcd
    if n < gcd:
        for i in range(n, 0, -1):
            if gcd % i == 0:
                break
            kills += 1
    print(kills)
