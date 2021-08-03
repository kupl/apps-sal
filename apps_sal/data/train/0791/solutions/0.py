tc = int(input())
for case in range(tc):
    n, d = list(map(int, input().split()))
    a = list(map(int, input().split()))
    sm = sum(a)
    f = True
    if sm % n == 0:
        avg = sm / n
        for i in range(d):
            tmp_sm = 0
            tmp_n = 0
            for j in range(i, n, d):
                tmp_sm = tmp_sm + a[j]
                tmp_n += 1
            if tmp_sm % tmp_n == 0:
                if avg != tmp_sm / tmp_n:
                    f = False
                    break
            else:
                f = False
                break
    else:
        f = False
    if f:
        ans = 0
        cur = 0
        for i in range(d):
            for j in range(i, n, d):
                cur = cur + avg - a[j]
                ans = ans + abs(cur)
        print(ans)
    else:
        print(-1)
