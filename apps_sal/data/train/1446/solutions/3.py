for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(2)
    else:
        if (n + 1) & n == 0:
            print(n // 2)
        else:
            print(-1)
