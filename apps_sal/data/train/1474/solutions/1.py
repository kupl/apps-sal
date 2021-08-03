for _ in range(int(input())):
    n = int(input())
    a = input().split()
    x = input()
    lis = []
    for i in range(n):
        count = 0
        for j in range(len(a[i])):
            if a[i][j] == x:
                count += 1
        lis.append(count)
    val = max(lis)
    for i in range(len(lis)):
        if lis[i] == val:
            print(a[i])
            break
