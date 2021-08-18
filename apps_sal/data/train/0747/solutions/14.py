for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    ss = set(a)
    j = max(a)
    s = []
    su = []
    flag = 1
    for i in ss:
        m = a.count(i)
        if m == 1:
            s.append(i)
        elif m == 2:
            s.append(i)
            su.append(i)
        else:
            flag = 0
            break
    if a.count(j) % 2 == 0:
        flag = 0
    if(flag):
        print("YES")
        s.sort()
        su.sort(reverse=True)
        print(*(s + su))
    else:
        print("NO")
