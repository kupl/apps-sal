T = int(input())
for j in range(T):
    n = int(input())
    ar = input()
    ar_v = list(map(int, input().split()))
    mx = 0
    for i in range(n - 7):
        sm = 0
        m = 1
        for k in range(8):
            if ar[i + k] == '.':
                sm += ar_v[k]
            elif ar[i + k] == 'd':
                sm = sm + 2 * ar_v[k]
            elif ar[i + k] == 't':
                sm = sm + 3 * ar_v[k]
            elif ar[i + k] == 'D':
                sm = sm + ar_v[k]
                m *= 2
            elif ar[i + k] == 'T':
                sm = sm + ar_v[k]
                m *= 3
        sm = sm * m
        if mx < sm:
            mx = sm
    print(mx)
