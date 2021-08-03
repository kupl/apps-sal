t = int(input())
for _ in range(t):
    n, k = list(map(int, input().strip().split()))
    a = list(map(int, input().strip().split()))
    c = 0
    f = 0
    b = []
    d = [0, 0]
    for i in range(n):
        if a[i] > k:
            f += 1
            if f == 1:
                d[0] = i
            else:
                if a[i] == a[d[0]]:
                    f -= 1
                else:
                    d[1] = i
        c += 1
        if f == 2:
            f = 1
            b.append(c - 1)
            c = d[1] - d[0]
            d[0] = d[1]
            d[1] = 0
    if len(b) == 0:
        print(c)
    else:
        print(max(b))
