(n, k) = [int(s) for s in input().split()]
s = [0 for i in range(k)]
a = [int(s) for s in input().split()]
b = [0 for i in range(n)]
b[0] = a[0]


def check():
    for i in range(1, n):
        b[i] = b[i - 1] + a[i]
    cnt = 0
    if b[n - 1] % k != 0:
        print('No')
        return
    m = b[n - 1] / k
    for j in range(0, n):
        if b[j] % m == 0:
            s[cnt] = j
            cnt += 1
    if cnt >= k:
        print('Yes')
        for i in range(k):
            if i == 0:
                print(s[i] + 1, end=' ')
            else:
                print(s[i] - s[i - 1], end=' ')
        return
    else:
        print('No')
        return


check()
