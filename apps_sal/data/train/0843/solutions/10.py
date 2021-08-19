for _ in range(int(input())):
    n = int(input())
    l = []
    for i in range(n):
        l1 = list(map(int, input().split()))
        l1.sort()
        l.append(l1)
    ans = l1[-1]
    p = ans
    for i in range(n - 2, -1, -1):
        flag = 0
        for j in range(n - 1, -1, -1):
            if l[i][j] < p:
                p = l[i][j]
                ans += p
                flag = 1
                break
        if flag == 0:
            print(-1)
            flag = 2
            break
    if flag != 2:
        print(ans)
