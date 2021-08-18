t = int(input())
while t > 0:
    n, p, q = input().split(" ")
    n = int(n)
    p = int(p)
    q = int(q)
    l = list(map(int, input().split(" ")))
    if q == 0:
        s = 0
        count = 0
        l.sort()
        for i in l:
            s = s + i
            if s > p:
                break
            else:
                count = count + 1
        print(count)

    t = t - 1
