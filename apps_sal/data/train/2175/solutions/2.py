n = int(input())
b = []
bb = []
for i in range(n):
    x = int(input())
    idx = 0
    for j in range(len(b)):
        nxt = b[j] ^ x
        if nxt < x:
            x = nxt
            idx ^= bb[j]
    if x == 0:
        cnt = 0
        v = []
        for k in range(2000):
            if idx & (1 << k):
                v.append(k)
        print(len(v), end=' ')
        for e in v:
            print(e, end=' ')
        print()
    else:
        print(0)
        idx ^= 1 << i
        b.append(x)
        bb.append(idx)
