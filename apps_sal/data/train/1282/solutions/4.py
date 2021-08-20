t = int(input())
while t:
    t -= 1
    (l, r) = [int(i) for i in input().split()]
    bl = bin(l)[2:]
    bl = bl[::-1]
    sub = 0
    val = 1
    ans = 0
    mod = 10 ** 9 + 7
    for i in range(len(bl)):
        if bl[i] == '1':
            ans += val * min(val - sub, r - l + 1) % mod
            sub += val
        val *= 2
    print(ans % mod)
