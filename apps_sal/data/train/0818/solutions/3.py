for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    (k, c) = ([], 0)
    for i in l:
        if i % 2 == 0:
            c += 1
        k.append(c)
    q = int(input())
    for i in range(q):
        (a, b) = map(int, input().split())
        a -= 1
        b -= 1
        if a == 0:
            if k[b] > 0:
                print('EVEN')
            else:
                print('ODD')
        else:
            a -= 1
            x = k[b] - k[a]
            if x > 0:
                print('EVEN')
            else:
                print('ODD')
