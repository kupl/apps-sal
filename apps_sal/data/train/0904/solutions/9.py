for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    t = 2
    f = []
    flag = 0
    if(x >= sum(a)):
        print("NO")
        continue
    f.append(max(a[-1], a[0]))
    while(t <= (n + 1) // 2):
        b = a[t - 1:n - t + 1]
        d = max(b[0], b[-1])
        e = min(b[0], b[-1])
        ind = 0
        flag1 = 0
        for i in range(len(f)):
            if(f[i] < d):
                continue
            else:
                flag1 = 1
                ind = i
                f.insert(ind, d)
                break
        if(flag1 == 0):
            f.append(d)
            ind = len(f)
        flag2 = 0
        for i in range(ind):
            if(f[i] < e):
                flag2 = 1
                f.remove(f[i])
                break
        if(flag2 == 1):
            flag3 = 0
            for i in range(len(f)):
                if(f[i] < e):
                    continue
                else:
                    flag3 = 1
                    inde = i
                    f.insert(inde, e)
                    break
            if(flag3 == 0):
                f.append(e)
                inde = len(f)

        t += 1
        if(sum(f) >= x):
            flag = 1
            print("YES")
            break
    if(flag == 0):
        if(sum(f) >= x):
            print("YES")
        else:
            print("NO")
