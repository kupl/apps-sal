for i in range(int(input())):
    a = list(map(int, input().split()))
    l = list(map(int, str(a[0])))
    t = len(set(l))

    if t == 3:
        print("27")
    elif t == 2:
        print("8")
    else:
        print("1")
