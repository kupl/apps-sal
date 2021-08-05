for i in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    v = 0
    for j, i in enumerate(a):
        if j % 2 == 0:
            if v < 0:
                v -= i
            else:
                v += i
        else:
            if v >= 0:
                v -= i
            else:
                v += i
    if abs(v) >= k:
        print(1)
    else:
        print(2)
