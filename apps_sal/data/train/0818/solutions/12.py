for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    m = int(input())
    prefix = [0 for i in range(n)]
    if l[0] % 2 == 0:
        prefix[0] = 1
    else:
        prefix[0] = 0
    for k in range(1, n):
        if l[k] % 2 == 0:
            prefix[k] = prefix[k - 1] + 1
        else:
            prefix[k] = prefix[k - 1]
    for i in range(m):
        (l, r) = list(map(int, input().split()))
        l -= 1
        r -= 1
        if prefix[r] - prefix[max(0, l - 1)] > 0:
            print('EVEN')
        else:
            print('ODD')
