(n, k) = map(int, input().split())
a = list(map(int, input().split()))
s = sum(a)
if s % k > 0:
    print('No')
else:
    p = s / k
    ar = []
    cur = 0
    l = 0
    for i in range(n):
        if a[i] + cur == p:
            ar.append(i - l + 1)
            l = i + 1
            cur = 0
            continue
        cur += a[i]
        if cur > p:
            print('No')
            break
    else:
        print('Yes')
        print(*ar)
