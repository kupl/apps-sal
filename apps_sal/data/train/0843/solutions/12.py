def maxScore():
    for t in range(int(input())):
        n = int(input())
        l = []
        for i in range(n):
            temp = sorted([int(x) for x in input().split()])
            l.append(temp)
        s = l[n - 1][n - 1]
        cdt_o = l[n - 1][n - 1]
        for i in range(n - 2, -1, -1):
            success = 1
            for j in range(n - 1, -1, -1):
                cdt_t = l[i][j]
                if cdt_t < cdt_o:
                    s += cdt_t
                    cdt_o = cdt_t
                    break
                elif j == 0:
                    success = 0
                    break
                elif cdt_t >= cdt_o:
                    continue
            if success == 0:
                break
        if success == 0:
            print(-1)
        else:
            print(s)


maxScore()
