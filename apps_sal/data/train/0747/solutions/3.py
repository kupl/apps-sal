t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    g = list(set(arr))
    g.sort()
    arr.sort()
    if len(g) == n:
        print("YES")
        print(*arr)
    else:
        f = 0
        k = []
        for i in g:
            c = arr.count(i)
            if c >= 3:
                f = 1
                break
            elif c == 2 and i == arr[-1]:
                f = 1
                break
            elif c == 2:
                k.append(i)
        k = sorted(k, reverse=True)
        g.extend(k)
        if f == 0:
            print("YES")
            print(*g)
        else:
            print("NO")
