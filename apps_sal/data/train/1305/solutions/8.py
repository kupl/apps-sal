for _ in range(int(input())):
    n = int(input())
    ar = [[0] * n] * n
    for i in range(n):
        ar[i] = list(map(int, input().split()))
    flag = 1
    for r in range(n - 1):
        for c in range(n - 1):
            if ar[r][c] == 1:
                if ar[r][c + 1] == 1:
                    flag = 0
                    break
                elif ar[r + 1][c] == 1:
                    flag = 0
                    break
    if flag == 1:
        print("SAFE")
    else:
        print("UNSAFE")
