try:
    t = int(input())
    result = []
    for i in range(t):
        check1 = True
        check2 = True
        tr = int(input())
        trl = list(map(int, input().split()))
        dr = int(input())
        drl = list(map(int, input().split()))
        ts = int(input())
        tsl = list(map(int, input().split()))
        ds = int(input())
        dsl = list(map(int, input().split()))

        for j in range(ts):
            if (tsl[j] not in trl):
                check1 = False
            else:
                continue

        for k in range(ds):
            if (dsl[k] not in drl):
                check2 = False
            else:
                continue

        if (check1 == True and check2 == True):
            result.append("yes")
        else:
            result.append("no")

    for b in result:
        print(b)


except:
    pass
