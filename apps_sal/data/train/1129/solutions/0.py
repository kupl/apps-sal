def fastpow(base, power):
    result = 1
    while power > 0:
        if power % 2 == 0:
            power = power // 2
            base = base * base
        else:
            power = power - 1
            result = result * base
            power = power // 2
            base = base * base
    return result


t = int(input())
for i in range(t):
    a = list(map(int, input().split()))
    (n, r) = (a[0], a[1])
    w = n * fastpow(n - 1, r) % (10 ** 9 + 7)
    print(w)
