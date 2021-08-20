t = int(input())
i = 0
while i < t:
    (n, k) = input().split()
    n = int(n)
    k = int(k)
    s = []
    ans = [0] * n
    s = input().split()
    j = 0
    while j < k:
        l = []
        l = input().split()
        m = 0
        while m < n:
            if s[m] in l:
                ans[m] = 1
            m += 1
        j += 1
    d = 0
    while d < n:
        if ans[d] == 0:
            print('NO', end=' ')
        else:
            print('YES', end=' ')
        d += 1
    print('')
    i += 1
