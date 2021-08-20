for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    l = list(map(int, input().split()))
    v = 0
    for i in range(n):
        if i % 2 == 0:
            if v < 0:
                v -= l[i]
            else:
                v += l[i]
        elif v < 0:
            v += l[i]
        else:
            v -= l[i]
    if abs(v) >= k:
        print('1')
    else:
        print('2')
