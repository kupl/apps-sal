n = int(input())
aSended = 0
bSended = 0
aPing = 0
bPing = 0
while n > 0:
    (t, x, y) = map(int, input().split())
    if t == 1:
        aSended = aSended + 10
        aPing = aPing + x
    elif t == 2:
        bSended = bSended + 10
        bPing = bPing + x
    n = n - 1
if int(aSended / 2) <= aPing:
    print('LIVE')
else:
    print('DEAD')
if int(bSended / 2) <= bPing:
    print('LIVE')
else:
    print('DEAD')
