for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in a:
        d[i] = d.get(i, 0) + 1
    if len(d) > 2:
        print(-1)
    elif len(d) == 1:
        for i in d:
            if i == n - 1 and d[i] == n:
                print(0)
            elif i == 0 and d[i] == n:
                print(n)
            else:
                print(-1)
    else:
        k = max(d.keys())
        if d.get(k - 1, 0) == k and d[k] == n - k:
            print(n - k)
        else:
            print(-1)
