t = int(input())
while t > 0:
    t -= 1
    l1 = ["" for _ in range(21)]
    n = int(input())
    l = input().split()
    ma = 0
    ans = ""
    for i in range(0, len(l[0])):
        s = ""
        for j in range(i, len(l[0])):
            s += l[0][j]
            fl = 1
            for k in range(1, len(l)):
                if s not in l[k]:
                    fl = 0
            if fl:
                le = len(s)
                if l1[le] == "":
                    l1[le] = s
                else:
                    l1[le] = min(l1[le], s)
                # print s,l1
    for i in range(20, 0, -1):
        if l1[i] != "":
            ans = l1[i]
            break
    print(ans)
