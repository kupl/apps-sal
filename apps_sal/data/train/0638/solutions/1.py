MOD = 1000000007
for t in range(int(input())):
    print('Case ' + str(t + 1) + ':')
    n, q = map(int, input().split())
    for i in range(q):
        x = input().strip()
        xlen = len(x)
        if xlen > n:
            print(0)
            continue
        rem = n - xlen
        remtot = pow(26, rem, MOD)
        ans = remtot * (rem + 1) % MOD
        print(ans)
