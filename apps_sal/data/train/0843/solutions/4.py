try:
    for i in range(int(input())):
        nm = int(input())
        lst = []
        for j in range(nm):
            lst.append(sorted([int(x) for x in input().split()]))
        sm = lst[-1][-1]
        mx = lst[-1][-1]
        c = 1
        for m in range(nm - 2, -1, -1):
            for n in range(nm - 1, -1, -1):
                if lst[m][n] < mx:
                    sm += lst[m][n]
                    mx = lst[m][n]
                    c += 1
                    break
        if c == nm:
            print(sm)
        else:
            print(-1)
except:
    pass
