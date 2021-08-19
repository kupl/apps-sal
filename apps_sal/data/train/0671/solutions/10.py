for _ in range(int(input())):
    (n, s) = list(map(int, input().split()))
    p = list(map(int, input().split()))
    l = list(map(int, input().split()))
    (l1, l2) = ([], [])
    for i in range(len(l)):
        if l[i] == 0:
            l1.append(p[i])
        elif l[i] == 1:
            l2.append(p[i])
    if len(l1) != 0 and len(l2) != 0:
        l1.sort()
        l2.sort()
        s += l1[0] + l2[0]
        if s <= 100:
            print('yes')
        else:
            print('no')
    else:
        print('no')
