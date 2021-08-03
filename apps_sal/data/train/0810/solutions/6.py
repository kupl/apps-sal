for _ in range(int(input())):
    n, q = map(int, input().split())
    x = [int(i) for i in input().split()]
    for j in range(q):
        f = 0
        l = [int(k) for k in input().split()]
        if(len(l) == 3):
            x[l[1]] = l[2]
        else:
            p = x[l[1]]
            r = x[0:l[1]]
            for m in range(l[1] + 1, len(x)):
                if(x[m] > p and x[m] not in r):
                    print(x[m])
                    f = 1
                    break
            if(f == 0):
                print(-1)
