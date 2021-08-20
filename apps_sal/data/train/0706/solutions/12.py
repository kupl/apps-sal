l = int(input())
for i in range(l):
    n = input().split()
    k = int(n[1])
    ws = list(map(int, input().split(' ')))
    flag = False
    for w in ws:
        if w > k:
            flag = True
            print(-1)
            break
    if flag:
        continue
    p = 0
    r = 0
    while p < len(ws):
        r = r + 1
        c = 0
        t = len(ws)
        while p < t and c + ws[p] <= k:
            c = c + ws[p]
            p = p + 1
    print(r)
