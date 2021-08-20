for _ in range(eval(input())):
    n = eval(input())
    mod = 1000000007
    (f1, f2) = ([0] * 101000, [0] * 101000)
    f1[1] = 0
    f1[2] = 2
    f1[3] = 3
    f2[1] = 1
    f2[2] = 1
    f2[3] = 2
    for i in range(4, 100001):
        f1[i] = f1[i - 1] % mod + f1[i - 2] % mod + f1[i - 3] % mod
        f2[i] = f2[i - 1] % mod + f2[i - 2] % mod + f2[i - 3] % mod
    print(f1[n] % mod, f2[n] % mod)
