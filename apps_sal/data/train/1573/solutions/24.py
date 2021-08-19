for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        print("NO")
    else:
        d = {}
        k = (n) * (n - 1) // 2
        r = k // n
        # print(r)
        l = [[0 for i in range(n)] for j in range(n)]
        # print(l)
        for i in range(1, n):
            # print(d.get(i,0))
            for j in range(i + 1, n + 1):
                if d.get(i, 0) < r:
                    l[i - 1][j - 1] = 1
                    d[i] = d.get(i, 0) + 1
                else:
                    l[j - 1][i - 1] = 1
                    d[j] = d.get(j, 0) + 1
        print("YES")
        for i in range(n):
            for j in range(n):
                print(l[i][j], end="")
            print()
