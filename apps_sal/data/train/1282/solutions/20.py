t = int(input())
while t > 0:
    a, b = list(map(int, input().split()))
    k = 1
    m = a
    n = b
    sum = 0
    x = 0
    y = 1
    while a > 0:
        a = a // 2
        l = m // k
        if l % 2 != 0:
            p = k * l
            q = k * (l + 1)
        else:
            p = k * (l + 1)
            q = k * (l + 2)
        k *= 2
        if m >= p and m < q:
            if b < q:
                o = b - m + 1
                lum = ((o % 1000000007) * (y % 1000000007)) % 1000000007
                sum = sum + lum
                sum = sum % 1000000007
            else:
                o = q - m
                lum = ((o % 1000000007) * (y % 1000000007)) % 1000000007
                sum = sum + lum
                sum = sum % 1000000007
        y *= 2
    print(sum)
    t -= 1
