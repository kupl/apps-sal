for _ in range(int(input())):
    n, m = map(int, input().split())
    ar = [int(x) for x in input().split()]
    ar.sort()
    f = 0
    j = 1
    # v=[]
    if m == 1:
        c = ar.count(1)
        if n - c == 0:
            print(-1)
        else:
            print(n - c)
    else:
        if ar[0] == 1:
            prev = 1
            j = 2
            for i in range(1, n):
                if ar[i] < m:
                    if ar[i] != prev and ar[i] == j:
                        j += 1
                        prev = ar[i]
                    elif ar[i] != prev and ar[i] != j:
                        f = 1
                        break
                    elif ar[i] == prev:
                        continue
                else:
                    break
        else:
            if m != 1:
                f = 1
        if f == 1 or j != m:
            print(-1)
        else:
            c = ar.count(m)
            if n - c == 0:
                print(-1)
            else:
                print(n - c)
