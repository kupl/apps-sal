T = int(input())
while T:
    s = input().split(' ')
    N = int(s[0])
    K = int(s[1])
    if N < K:
        print('0')
    else:
        p = max(K, N - K)
        q = min(K, N - K)
        res = 1
        while N > p:
            res *= N
            N -= 1
        while q > 1:
            res /= q
            q -= 1
        print(res)
    T -= 1
