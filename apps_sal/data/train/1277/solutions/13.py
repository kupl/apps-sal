t = int(input())
for i in range(t):
    n = int(input())
    res = []
    initialprice = 0
    middleprice = 0
    finalprice = 0
    totalloss = 1
    loss = 0
    for i in range(n):
        (p, q, d) = list(map(float, input().split()))
        initialprice = p
        middleprice = initialprice + initialprice * d / 100
        finalprice = middleprice - middleprice * d / 100
        loss = initialprice - finalprice
        totalloss = float(q * loss)
        res.append(totalloss)
    print(float(sum(res)))
