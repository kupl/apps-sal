for _ in range(int(input())):
    n = int(input())
    mid = n // 2
    for i in range(n):
        if(i > mid):
            break
        print(" " * i + "*")

    for i in range(mid - 1, -1, -1):
        print(" " * i + "*")
