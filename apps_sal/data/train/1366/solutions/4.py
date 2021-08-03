for _ in range(0, int(input())):
    n = int(input())
    a = list(map(int, input().split(" ")))
    start = -1
    end = -1
    for i in range(0, n):
        if a[i] != 0:
            start = i
            break
    for i in range(len(a) - 1, -1, -1):
        if a[i] != 0:
            end = i
            break
    if start == end:
        print(1)
    else:
        print(end - start + 1)
