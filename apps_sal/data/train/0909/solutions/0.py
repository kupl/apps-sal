for u in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    d = list(map(int, input().split()))
    ka = []
    k = []
    l.sort()
    d.sort()
    for i in range(n):
        ka.append(d[i])
        ka.append(l[i])
    for i in range(n):
        k.append(l[i])
        k.append(d[i])
    if(ka == sorted(ka)):
        print("YES")
    elif(k == sorted(k)):
        print("YES")
    else:
        print("NO")
