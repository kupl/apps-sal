testcases = int(input())
for testcase in range(testcases):
    temparr = input()
    temparr = temparr.split()
    x = int(temparr[0])
    y = int(temparr[1])
    n = int(temparr[2])
    if x == y:
        print(0)
        continue
    diffbit = 0
    biggestnum = 1 << 5
    checknum = 0
    flag = 0
    while True:
        curx = x & biggestnum
        cury = y & biggestnum
        if curx == cury:
            biggestnum = biggestnum >> 1
            continue
        checknum = biggestnum
        if curx:
            flag = 1
        break
    ans = 0
    for i in range(n + 1):
        if flag == 1:
            if i & checknum:
                ans += 1
        elif i & checknum == 0:
            ans += 1
    print(ans)
