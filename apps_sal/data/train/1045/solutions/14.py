for _ in range(int(input().strip())):
    s = list(input().strip())
    n = len(s)
    MOD = 1000000007
    vow = ['a', 'e', 'i', 'o', 'u']
    K = ''
    for i in range(n):
        if s[i] not in vow:
            K = K + '1'
        else:
            K = K + '0'
    co = int(K, 2)
    print(str(co % MOD))
