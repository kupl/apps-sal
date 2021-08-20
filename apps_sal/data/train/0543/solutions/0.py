for _ in range(int(input())):
    tr = int(input())
    trl = list(map(int, input().split()))
    dr = int(input())
    drl = list(map(int, input().split()))
    ts = int(input())
    tsl = list(map(int, input().split()))
    ds = int(input())
    dsl = list(map(int, input().split()))
    for item in tsl:
        if item in trl:
            res = 1
            continue
        else:
            res = 0
            break
    for item1 in dsl:
        if item1 in drl:
            res1 = 1
            continue
        else:
            res1 = 0
            break
    if res == 1 and res1 == 1:
        print('yes')
    else:
        print('no')
