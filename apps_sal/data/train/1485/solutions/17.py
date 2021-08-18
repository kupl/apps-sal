for __ in range(int(input())):
    n = int(input())
    a = []
    ans = 10**9
    for _ in range(n):
        a.append(list(input()))
    l1, l2, acnt, bcnt, diff = [], [], 0, 0, []
    for i in range(n):
        acnt, bcnt = 0, 0
        for j in range(len(a[i]) // 2):
            if(a[i][j] == '1'):
                acnt += 1
            if(a[i][n - 1 - j] == '1'):
                bcnt += 1
        l1.append(acnt)
        l2.append(bcnt)
    acnt, bcnt = sum(l1), sum(l2)
    if(acnt == bcnt):
        print("0")
    elif(abs(bcnt - acnt) == 1):
        print("1")
    else:
        if(bcnt > acnt):
            l1, l2 = l2, l1
            acnt, bcnt = bcnt, acnt
        for i in range(n):
            val = l1[i] - l2[i]
            diff.append(val if(val > 0) else 0)
        for i in range(len(diff)):
            ans = min(ans, abs(acnt - diff[i] - bcnt - diff[i]))
        print(ans)
