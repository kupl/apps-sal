for u in range(int(input())):
    l = list(map(int, input().split()))
    d = list(map(int, input().split()))
    c = []
    f = 0
    for i in range(3):
        if(d[i] < l[i]):
            f = 1
            break
    if(f == 1):
        print(-1)
    else:
        s = 0
        for i in range(3):
            s = s + d[i] - l[i]
        print(s)
