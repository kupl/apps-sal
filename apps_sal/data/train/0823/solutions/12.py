t = int(input())
for _ in range(t):
    ar = list(map(int, input().split()))
    ok = False
    for i in range(1, 16):
        csum = 0
        for j in range(len(ar)):
            if i & 1 << j > 0:
                csum += ar[j]
        if csum == 0:
            ok = True
            break
    if ok:
        print('Yes')
    else:
        print('No')
