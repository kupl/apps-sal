t = int(input())
for _ in range(t):
    n = int(input())
    ll = list(map(int, input().split()))
    ss = 0
    for ele in ll:
        if ele <= 6:
            ss += ele
        else:
            zz = ele % 6
            if zz == 0:
                ss += 6
            else:
                ss += zz
    print(ss)
