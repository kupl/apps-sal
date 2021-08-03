for t in range(int(input())):
    a, b, c = list(map(int, input().split()))
    l = []
    l.append(a)
    l.append(b)
    l.append(c)
    l.sort()
    if(l[2] <= ((l[0] + l[1]) + 1)):
        print("Yes")
    else:
        print("No")
