t = int(input())
for o in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    q = int(input())
    l1 = []
    c = 0
    for i in l:
        if i % 2 == 0:
            c += 1
            l1.append(c)
        else:
            l1.append(c)
    for v in range(q):
        (l, r) = map(int, input().split())
        l -= 1
        r -= 1
        if l == 0:
            if l1[r] > 0:
                print('EVEN')
            else:
                print('ODD')
        else:
            l -= 1
            x = l1[r] - l1[l]
            if x > 0:
                print('EVEN')
            else:
                print('ODD')
