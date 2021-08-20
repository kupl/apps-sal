for _ in range(int(input())):
    (n, k) = [int(x) for x in input().split()]
    a = list(map(int, input().split()))
    s = set(a)
    s = list(s)
    aa = []
    f = 0
    for i in range(n - k + 1):
        f = 0
        ss = a[i:i + k]
        for j in range(len(s)):
            if s[j] not in ss:
                f = 1
                break
        if f == 0:
            aa.append(sum(ss))
    print(max(aa))
