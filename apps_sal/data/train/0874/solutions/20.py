t = int(input())
for q in range(t):
    u = 0
    nch = 0
    (ch, d, h) = list(map(int, input().split()))
    l = sorted(list(map(int, input().split())))
    for i in l:
        k = (i - 1) // h + 1
        if k < 3:
            u += k
            if u > d:
                break
            else:
                nch += 1
        else:
            break
    print(nch)
