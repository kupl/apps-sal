for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = [[a[i], i]for i in range(n)]
    b.sort()
    c = [0] * n
    for i in range(n):
        x = b[i][0]
        if a[b[(i + (n // 2)) % n][1]] == x:
            print("No")
            break
        else:

            c[b[(i + (n // 2)) % n][1]] = x
    else:
        print("Yes")
        print(*c)
