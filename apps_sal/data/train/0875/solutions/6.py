for i in range(int(input())):
    n, z1, z2 = map(int, input().split())
    arr = list(map(int, input().split()))
    m = dict()
    for item in arr:
        m[item] = 1
        m[-item] = -1
    if z1 in m or z2 in m:
        print("1")
    else:
        cnt = 0
        for item in arr:
            if z1 - item in m or z2 - item in m:
                cnt += 1
            if z1 + item in m or z2 + item in m:
                cnt += 1
        if cnt == 2 * n:
            print("2")
        else:
            print("0")
