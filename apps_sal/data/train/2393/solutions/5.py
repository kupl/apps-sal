for _ in range(int(input())):
    n = int(input())
    ar = []
    for i in range(n):
        ar.append(list(map(int, input())))
    ans = 'YES'
    for i in range(n - 1):
        for j in range(n - 1):
            if ar[i][j] == 1:
                flag = 0
                if 0 <= i + 1 <= n - 1 and ar[i + 1][j] == 1:
                    flag = 1
                elif 0 <= j + 1 <= n - 1 and ar[i][j + 1] == 1:
                    flag = 1
                if flag == 0:
                    ans = 'NO'
                    break
    print(ans)
