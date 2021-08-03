for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    if m < 9:
        print(0, 0)
    else:
        m = str(m)
        if len(m) > 1:
            no = len(m) - 1
        else:
            no = 1
        res = n * no
        print(res, n)
