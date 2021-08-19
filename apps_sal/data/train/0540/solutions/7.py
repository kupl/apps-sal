# cook your dish here
for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    l = list(map(int, input().split()))
    c, cnt = m - 1, 0
    l1 = [0] * m

    for k in l:
        if k < m:
            if l1[k] == 0:
                l1[k] = 1
                c -= 1
            cnt += 1

        elif k > m:
            cnt += 1

    if c == 0:
        print(cnt)

    else:
        print(-1)
