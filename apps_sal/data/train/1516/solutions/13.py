for i in range(int(input())):
    n, k = [int(i) for i in input().split()]
    mod = 1000000007
    c = (k - 1) % mod
    dif = (2 * k) - (n + k - 1) - 1
    if dif > 0:
        no = dif // (n - 1)
        if dif % (n - 1) != 0:
            no += 1
        c = (c + (no * (2 * dif - (no - 1) * (n - 1)) // 2) % mod) % mod
    print(c)
