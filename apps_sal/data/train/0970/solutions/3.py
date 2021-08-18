for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    q = int(input())
    h = []
    for i in range(q):
        x, y = list(map(int, input().split()))
        f, c, g = x + y, 0, 0
        b, m = 0, n - 1
        while(b <= m):
            i = (b + m) // 2
            if l[i] == f:
                g = 1
                break
            elif l[i] > f:
                m = i - 1
            else:
                b = i + 1
        if g == 1:
            print(-1)
        else:
            if l[i] > f:
                print(i)
            else:
                print(i + 1)
